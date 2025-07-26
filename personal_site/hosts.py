from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'personal_site.urls', name='www'),
    host(r'resume', 'personal_site.urls', name='resume'),
    host(r'blog', 'personal_site.blog_urls', name='blog'),
)
