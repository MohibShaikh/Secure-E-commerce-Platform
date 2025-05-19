from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from aiwaf.models import BlockedIP, DynamicKeyword
from django.db.models import Count
from datetime import datetime, timedelta

@staff_member_required
@require_http_methods(["GET"])
def waf_monitor(request):
    # Get last 24 hours of data
    last_24h = datetime.now() - timedelta(hours=24)
    
    # Get blocked IPs
    blocked_ips = BlockedIP.objects.filter(
        created_at__gte=last_24h
    ).values('ip_address').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    # Get top attack patterns
    attack_patterns = DynamicKeyword.objects.filter(
        created_at__gte=last_24h
    ).values('keyword').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    # Get rate limit stats
    rate_limits = BlockedIP.objects.filter(
        created_at__gte=last_24h,
        reason__startswith='rate_limit'
    ).count()
    
    # Get anomaly stats
    anomalies = BlockedIP.objects.filter(
        created_at__gte=last_24h,
        reason__startswith='anomaly'
    ).count()
    
    return JsonResponse({
        'last_24h_stats': {
            'total_blocks': BlockedIP.objects.filter(created_at__gte=last_24h).count(),
            'rate_limit_blocks': rate_limits,
            'anomaly_blocks': anomalies,
            'top_blocked_ips': list(blocked_ips),
            'top_attack_patterns': list(attack_patterns),
        },
        'waf_status': {
            'rate_limit_window': '10 seconds',
            'max_requests': '20 per window',
            'flood_threshold': '10 requests',
            'anomaly_window': '60 seconds',
        }
    }) 