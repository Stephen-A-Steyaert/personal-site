from django_hosts import patterns, host # type: ignore
from typing import cast, Any

host_patterns: list[Any] = cast(
    list[Any],
    patterns(
        '',
        host(r'www', 'personal_site.urls', name='www'),
        host(r'resume', 'personal_site.urls', name='resume'),
        host(r'blog', 'personal_site.blog_urls', name='blog'),
    )
)