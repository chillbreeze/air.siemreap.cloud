# Blog settings
SITENAME = 'Air Quality - Siem Reap'
SITESUBTITLE = 'Notes from Siem Reap'
SITEURL = 'https://air.siemreap.cloud/blog'

# Author
AUTHOR = 'Terry'

# Paths
PATH = 'content'
OUTPUT_PATH = 'output'

# Timezone and language
TIMEZONE = 'Asia/Phnom_Penh'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Don't generate feeds for now - keep it simple
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Keep URLs clean
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Don't generate things we don't need
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

# Theme
THEME = 'theme'

# Pagination
DEFAULT_PAGINATION = 10
