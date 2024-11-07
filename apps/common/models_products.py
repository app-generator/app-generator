from django.db import models
from django_quill.fields import QuillField
from django.utils import crypto
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.text import slugify
from autoslug import AutoSlugField

from .models_base import *

# Create your models here.

class Type(models.TextChoices):
    WEBAPP = 'WEBAPP', 'WebApp'
    DASHBOARD = 'DASHBOARD', 'Dashboard'
    API = 'API', 'Api'

class Design(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'

    DATTA_ABLE              = 'datta-able'              , 'datta-able'
    DATTA_ABLE_PRO          = 'datta-able-pro'          , 'datta-able-pro'

    GRADIENT_ABLE           = 'gradient-able'           , 'gradient-able'
    GRADIENT_ABLE_PRO       = 'gradient-able-pro'       , 'gradient-able-pro'

    BERRY_DASHBOARD         = 'berry-dashboard'         , 'berry-dashboard'
    BERRY_DASHBOARD_PRO     = 'berry-dashboard-pro'     , 'berry-dashboard-pro'

    VOLT_DASHBOARD          = 'volt-dashboard'          , 'volt-dashboard'
    VOLT_DASHBOARD_PRO      = 'volt-dashboard-pro'      , 'volt-dashboard-pro'

    SOFT_DASHBOARD          = 'soft-ui-dashboard'       , 'soft-ui-dashboard'
    SOFT_DASHBOARD_PRO      = 'soft-ui-dashboard-pro'   , 'soft-ui-dashboard-pro'

    MATERIAL_DASHBOARD      = 'material-dashboard'      , 'material-dashboard'
    MATERIAL_DASHBOARD_PRO  = 'material-dashboard-pro'  , 'material-dashboard-pro'
    MATERIAL_DASHBOARD2_PRO = 'material-dashboard2-pro' , 'material-dashboard2-pro'

    ARGON_DASHBOARD         = 'argon-dashboard'         , 'argon-dashboard'
    ARGON_DASHBOARD_PRO     = 'argon-dashboard-pro'     , 'argon-dashboard-pro'
    ARGON_DASHBOARD2_PRO    = 'argon-dashboard2-pro'    , 'argon-dashboard2-pro'

    BLACK_DASHBOARD         = 'black-dashboard'         , 'black-dashboard'
    BLACK_DASHBOARD_PRO     = 'black-dashboard-pro'     , 'black-dashboard-pro'

    ADMINLTE                = 'adminlte'                , 'adminlte'
    ADMINLTE_PRO            = 'adminlte-pro'            , 'adminlte-pro'

    COREUI                  = 'coreui'                  , 'coreui'
    COREUI_PRO              = 'coreui-pro'              , 'coreui-pro'

    MATERIAL_KIT            = 'material-kit'            , 'material-kit'
    MATERIAL_KIT_PRO        = 'material-kit-pro'        , 'material-kit-pro'

    ARGON_DESIGN            = 'argon-design'            , 'argon-design'
    ARGON_DESIGN_PRO        = 'argon-design-pro'        , 'argon-design-pro'

    PIXEL_DESIGN            = 'pixel-bootstrap'         , 'pixel-bootstrap'
    PIXEL_DESIGN_PRO        = 'pixel-bootstrap-pro'     , 'pixel-bootstrap-pro'

    SOFT_DESIGN             = 'soft-ui-design'          , 'soft-ui-design'
    SOFT_DESIGN_PRO         = 'soft-ui-design-pro'      , 'soft-ui-design-pro'

    # RAW Kits
    BOOTSTRAP_DESIGN        = 'bootstrap-design'        , 'bootstrap-design'
    FLOWBITE_DESIGN         = 'flowbite'                , 'flowbite'
    TAILWIND_DESIGN         = 'tailwind'                , 'tailwind'
    MUI_DESIGN              = 'mui'                     , 'mui'
    SHADCN_DESIGN           = 'shadcn'                  , 'shadcn'
    BULMA_DESIGN            = 'bulma'                   , 'bulma'
    PURE_CSS_DESIGN         = 'pure-css'                , 'pure-css'

class DesignBy(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    CREATIVE_TIM            = 'creative-tim'            , 'creative-tim'
    CODEDTHEMES             = 'codedthemes'             , 'codedthemes'
    THEMESBERG              = 'themesberg'              , 'themesberg'
    APPSEED                 = 'appseed'                 , 'appseed'
    ADMINLTE                = 'adminlte'                , 'adminlte'
    COREUI                  = 'coreui'                  , 'coreui'
    TAILWIND                = 'tailwind'                , 'tailwind'
    FLOWBITE                = 'flowbite'                , 'flowbite'
    BOOTSTRAP               = 'bootstrap'               , 'bootstrap'    

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
    MUI                     = 'mui'                     , 'mui'

class Tech1(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    API_SERVER              = 'api-server'              , 'api-server'
    DJANGO                  = 'django'                  , 'django'
    FLASK                   = 'flask'                   , 'flask'
    FAST_API                = 'fast-api'                , 'fast-api'
    NODEJS                  = 'nodejs'                  , 'nodejs'
    LARAVEL                 = 'laravel'                 , 'laravel'
    NEXTJS                  = 'nextjs'                  , 'nextjs'
    FULLSTACK               = 'full-stack'              , 'full-stack'

class Tech2(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    REACT                   = 'react'                   , 'react'
    VUE                     = 'vuejs'                   , 'vuejs'
    SVELTE                  = 'svelte'                  , 'svelte'

class Tech3(models.TextChoices):

    DEFAULT                 = 'NA'                      , 'NA'
    DOCKER                  = 'docker'                  , 'docker'
    K8S                     = 'kubernetes'              , 'kubernetes'
    CONTAINERD              = 'containerd'              , 'containerd'
    VM                      = 'virtual-machine'         , 'virtual-machine'
    PROXMOX                 = 'proxmox'                 , 'proxmox'
    PODMAN                  = 'podman'                  , 'podman'


class ProductTag(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class ProductVideo(BaseModel):
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.url

class Products(BaseModel):
    name            = models.CharField(max_length=255)
    type            = models.CharField(max_length=24, choices=Type.choices, default=Type.DASHBOARD) 
    tags            = models.ManyToManyField(ProductTag, blank=True)

    card_info       = models.CharField(max_length=128,     default='')                                              # Short Sentence (used on cards)
    info            = models.CharField(max_length=256,     default='')                                              # Long Sentence - Used on pages
    
    features        = QuillField(null=True, blank=True)                                                             # Full Information about the product.

    seo_title       = models.CharField(max_length=128,  default='')                                                 # SEO Title
    seo_tags        = models.CharField(max_length=128,  default='')                                                 # SEO Tags
    seo_description = models.CharField(max_length=256,  default='')                                                 # SEO Description

    canonical       = models.CharField(max_length=128,  default='')

    code            = models.CharField(max_length=128,  unique=True)                                                # Product code
    slug            = models.CharField(max_length=128,  unique=True)                                                # used for migration  

    free            = models.BooleanField(default=True)                                                             # Free or PAID

    price           = models.IntegerField(default=0)                                                                # The Price for Personal Lic   
    price2          = models.IntegerField(default=0)                                                                # The Price for Company Lic   

    pay_url         = models.CharField(max_length=256, null=True, blank=True)                                       # Pay URL  (used by Personal Lic
    pay_url2        = models.CharField(max_length=256, null=True, blank=True)                                       # Pay URL  (used by price2) 

    url_dw          = models.CharField(max_length=256, default=None)                                                # Download Link
    url_demo        = models.CharField(max_length=256, default=None)                                                # DEMO URL
    url_docs        = models.CharField(max_length=256, default=None)                                                # Documentation
    url_blog        = models.CharField(max_length=256, null=True, blank=True)                                       # Blog Article 
    url_video       = models.CharField(max_length=256, null=True, blank=True)                                       # Blog Article 
    url_changelog   = models.CharField(max_length=256, default=None)                                                # Release notes
    url_readme      = models.CharField(max_length=256, default=None)                                                # README 

    design          = models.CharField(max_length=24, choices=Design.choices,       default=Design.DEFAULT)         # material dashboard2, adminlte 
    design_by       = models.CharField(max_length=24, choices=DesignBy.choices,     default=DesignBy.DEFAULT)       # creative-tim, codedthemes
    design_system   = models.CharField(max_length=24, choices=DesignSystem.choices, default=DesignSystem.DEFAULT)   # soft ui design, material design
    design_css      = models.CharField(max_length=24, choices=CssSystem.choices,    default=CssSystem.DEFAULT)      # soft ui design, material design

    tech1           = models.CharField(max_length=24, choices=Tech1.choices,       default=Tech1.DEFAULT)           # Primary Tech   (backend)
    tech2           = models.CharField(max_length=24, choices=Tech2.choices,       default=Tech2.DEFAULT)           # Secondary Tech (frontend)
    tech3           = models.CharField(max_length=24, choices=Tech2.choices,       default=Tech3.DEFAULT)           # Related tech   (related-alike-1) -> Docker
    tech4           = models.CharField(max_length=64, null=True, blank=True)                                        # Related tech   (related-alike-2) -> Vite ..etc 
    tech5           = models.CharField(max_length=64, null=True, blank=True)                                        # Related tech   (related-alike-3) -> AI

    downloads       = models.IntegerField(default=0)

    related_product = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        related_name='related_products', 
        null=True, 
        blank=True
    )

    release_date    = models.DateField(null=True, blank=True)
    version         = models.CharField(max_length=20, null=True, blank=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"design": self.design, "tech1": self.tech1})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if not self.free:
            if not self.pay_url:
                raise ValidationError({'pay_url': 'This field is required.'})
            # if not self.pay_url2:
            #     raise ValidationError({'pay_url2': 'This field is required.'})
    
    def __str__(self):
        return self.name


class CategoryChoices(models.TextChoices):
    DOWNLOAD = 'DOWNLOAD', 'Downlaod'
    FEATURE = 'FEATURE', 'Feature'
    PROMO_NAME = 'PROMO_NAME', 'Promo Name'
    PROMO_COUPON = 'PROMO_COUPON', 'Promo Coupon'
    PROMO_DISCOUNT = 'PROMO_DISCOUNT', 'Promo Discount'
    PROMO_INFO = 'PROMO_INFO', 'Promo Info'
    PROMO_END_DATE = 'PROMO_END_DATE', 'Promo End Date'
    URL_VIDEO = 'URL_VIDEO', 'Video URL'
    URL_DOCS = 'URL_DOCS', 'Docs URL'
    URL_BLOG = 'URL_BLOG', 'Blog URL'

class Props(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=250, choices=CategoryChoices.choices)
    state = models.BooleanField(default=False)
    data = models.CharField(max_length=255)
    order = models.IntegerField(null=True, blank=True)

class Download(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    downloaded_version = models.CharField(max_length=20, null=True, blank=True)
    downloaded_release_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.downloaded_version = self.product.version
        self.downloaded_release_date = self.product.release_date
        super().save(*args, **kwargs)