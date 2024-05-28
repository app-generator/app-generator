from django.db import models
from django_quill.fields import QuillField
from django.utils import crypto

# Create your models here.

class Type(models.TextChoices):
    WEBAPP = 'WEBAPP', 'WebApp'
    DASHBOARD = 'DASHBOARD', 'Dashboard'
    API = 'API', 'Api'

class Design(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'

    DATTA_ABLE              = 'datta-able'              , 'datta-able'
    DATTA_ABLE_PRO          = 'datta-able-pro'          , 'datta-able-pro'

    SOFT_DASHBOARD          = 'soft-ui-dashboard'       , 'soft-ui-dashboard'
    SOFT_DASHBOARD_PRO      = 'soft-ui-dashboard-pro'   , 'soft-ui-dashboard-pro'

    MATERIAL_DASHBOARD      = 'material-dashboard'      , 'material-dashboard'
    MATERIAL_DASHBOARD_PRO  = 'material-dashboard-pro'  , 'material-dashboard-pro'
    MATERIAL_DASHBOARD2_PRO = 'material-dashboard2-pro' , 'material-dashboard2-pro'

    ARGON_DASHBOARD         = 'argon-dashboard'         , 'material-dashboard'
    ARGON_DASHBOARD_PRO     = 'argon-dashboard-pro'     , 'material-dashboard-pro'
    ARGON_DASHBOARD2_PRO    = 'argon-dashboard2-pro'    , 'material-dashboard2-pro'

class DesignBy(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    CREATIVE_TIM            = 'creative-tim'            , 'creative-tim'
    CODEDTHEMES             = 'codedthemes'             , 'codedthemes'
    THEMESBERG              = 'themesberg'              , 'themesberg'
    APPSEED                 = 'appseed'                 , 'appseed'

class DesignSystem(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    SOFT_DESIGN             = 'soft-ui-design'          , 'soft-ui-design'
    MATERIAL_DESIGN         = 'material-design'         , 'material-design'
    ARGON_DESIGN            = 'argon-design'            , 'argon-design'
    BLACK_DESIGN            = 'black-design'            , 'black-design'
    FLOWBITE                = 'flowbite'                , 'flowbite'

class CssSystem(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    BOOTSTRAP               = 'bootstrap'               , 'bootstrap'
    BOOTSTRAP4              = 'bootstrap4'              , 'bootstrap4'
    BOOTSTRAP5              = 'bootstrap5'              , 'bootstrap5'
    TAILWIND                = 'tailwind'                , 'tailwind'

class Tech1(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    API_SERVER              = 'api-server'              , 'api-server'
    DJANGO                  = 'django'                  , 'django'
    FLASK                   = 'flask'                   , 'flask'
    NODEJS                  = 'nodejs'                  , 'nodejs'
    LARAVEL                 = 'laravel'                 , 'laravel'
    NEXTJS                  = 'nextjs'                  , 'nextjs'
    FULLSTACK               = 'full-stack'              , 'full-stack'

class Tech2(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    REACT                   = 'react'                   , 'react'
    VUE                     = 'vuejs'                   , 'vuejs'
    NEXTJS                  = 'nextjs'                  , 'nextjs'
    SVELTE                  = 'svelte'                  , 'svelte'

class Tech3(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    DOCKER                  = 'docker'                  , 'docker'
    K8S                     = 'kubernetes'              , 'kubernetes'
    CONTAINERD              = 'containerd'              , 'containerd'
    VM                      = 'virtual-machine'         , 'virtual-machine'
    PROXMOX                 = 'proxmox'                 , 'proxmox'


def get_thumbnail_filename(instance, filename):
    ext = filename.split('.')[-1]
    return f"product/{instance.design_system}/{instance.tech1}/thumbnail_{crypto.get_random_string(7)}.{ext}"

class Products(models.Model):

    thumbnail       = models.ImageField(upload_to=get_thumbnail_filename, blank=True)
    name            = models.CharField(max_length=255)
    type            = models.CharField(max_length=24, choices=Type.choices, default=Type.WEBAPP) 

    info            = models.CharField(max_length=128,     default='')                                              # Short Sentence (used on cards)
    
    features        = QuillField()                                                                                  # Full Information about the product.
    documentation   = QuillField()                                                                                  # Markdown

    seo_title       = models.CharField(max_length=128,  default='')                                                 # SEO Title
    seo_tags        = models.CharField(max_length=128,  default='')                                                 # SEO Tags
    seo_description = models.CharField(max_length=256,  default='')                                                 # SEO Description

    canonical       = models.CharField(max_length=128,  default='')

    code            = models.CharField(max_length=128,  unique=True)                                                # Product code
    slug            = models.CharField(max_length=128,  unique=True)                                                # used for migration  

    free            = models.BooleanField(default=True)                                                             # Free or PAID

    price           = models.IntegerField(default=0)                                                                # The Price for Personal Lic   
    price2          = models.IntegerField(default=0)                                                                # The Price for Company Lic   

    pay_url         = models.CharField(max_length=256, default=None)                                                # Pay URL  (used by Personal Lic
    pay_url2        = models.CharField(max_length=256, default=None)                                                # Pay URL  (used by price2) 

    url_dw          = models.CharField(max_length=256, default=None)                                                # Download Link
    url_demo        = models.CharField(max_length=256, default=None)                                                # DEMO URL
    url_docs        = models.CharField(max_length=256, default=None)                                                # Documentation
    url_blog        = models.CharField(max_length=256, default=None)                                                # Blog Article 
    url_video       = models.CharField(max_length=256, default=None)                                                # yTube URL  
    url_changelog   = models.CharField(max_length=256, default=None)                                                # Release notes
    url_readme      = models.CharField(max_length=256, default=None)                                                # README 

    design          = models.CharField(max_length=24, choices=Design.choices,       default=Design.DEFAULT)         # material dashboard2, adminlte 
    design_by       = models.CharField(max_length=24, choices=DesignBy.choices,     default=DesignBy.DEFAULT)       # creative-tim, codedthemes
    design_system   = models.CharField(max_length=24, choices=DesignSystem.choices, default=DesignSystem.DEFAULT)   # soft ui design, material design
    design_css      = models.CharField(max_length=24, choices=CssSystem.choices,    default=CssSystem.DEFAULT)      # soft ui design, material design

    tech1           = models.CharField(max_length=24, choices=Tech1.choices,       default=Tech1.DEFAULT)           # Primary Tech   (backend)
    tech2           = models.CharField(max_length=24, choices=Tech2.choices,       default=Tech2.DEFAULT)           # Secondary Tech (frontend)
    tech3           = models.CharField(max_length=24, choices=Tech2.choices,       default=Tech3.DEFAULT)           # Related tech   (related-alike-1) -> Docker
    tech4           = models.CharField(max_length=64, default=None)                                                # Related tech   (related-alike-2) -> Vite ..etc 
    tech5           = models.CharField(max_length=64, default=None)                                                # Related tech   (related-alike-3) -> AI

    downloads       = models.IntegerField(default=0)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
