from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from aiwaf.models import BlacklistEntry, DynamicKeyword, FeatureSample
from django.db.models import Count
from datetime import datetime, timedelta

@staff_member_required
@require_http_methods(["GET"])
def waf_monitor(request):
    # Get last 24 hours of data
    last_24h = datetime.now() - timedelta(hours=24)
    
    # Get blacklisted IPs
    blacklisted_ips = BlacklistEntry.objects.filter(
        created_at__gte=last_24h
    ).values('ip_address', 'reason').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    # Get top attack patterns
    attack_patterns = DynamicKeyword.objects.filter(
        last_updated__gte=last_24h
    ).values('keyword', 'count').order_by('-count')[:10]
    
    # Get anomaly stats
    anomalies = FeatureSample.objects.filter(
        created_at__gte=last_24h,
        label='anomaly'
    ).count()
    
    # Get rate limit stats
    rate_limits = BlacklistEntry.objects.filter(
        created_at__gte=last_24h,
        reason__startswith='rate_limit'
    ).count()
    
    return JsonResponse({
        'last_24h_stats': {
            'total_blocks': BlacklistEntry.objects.filter(created_at__gte=last_24h).count(),
            'rate_limit_blocks': rate_limits,
            'anomaly_blocks': anomalies,
            'top_blocked_ips': list(blacklisted_ips),
            'top_attack_patterns': list(attack_patterns),
        },
        'waf_status': {
            'rate_limit_window': '10 seconds',
            'max_requests': '20 per window',
            'flood_threshold': '10 requests',
            'anomaly_window': '60 seconds',
        }
    }) 