from ...attribute import models as attribute_models
from ...core.tracing import traced_resolver
from ...discount import models as discount_models
from ...menu import models as menu_models
from ...page import models as page_models
from ...product import models as product_models
from ...shipping import models as shipping_models
from ...site import models as site_models
from . import dataloaders

TYPE_TO_TRANSLATION_LOADER_MAP = {
    attribute_models.Attribute: (
        dataloaders.AttributeTranslationByIdAndLanguageCodeLoader
    ),
    attribute_models.AttributeValue: (
        dataloaders.AttributeValueTranslationByIdAndLanguageCodeLoader
    ),
    product_models.Category: (dataloaders.CategoryTranslationByIdAndLanguageCodeLoader),
    product_models.Collection: (
        dataloaders.CollectionTranslationByIdAndLanguageCodeLoader
    ),
    menu_models.MenuItem: (dataloaders.MenuItemTranslationByIdAndLanguageCodeLoader),
    page_models.Page: dataloaders.PageTranslationByIdAndLanguageCodeLoader,
    product_models.Product: (dataloaders.ProductTranslationByIdAndLanguageCodeLoader),
    product_models.ProductVariant: (
        dataloaders.ProductVariantTranslationByIdAndLanguageCodeLoader
    ),
    discount_models.Sale: dataloaders.SaleTranslationByIdAndLanguageCodeLoader,
    shipping_models.ShippingMethod: (
        dataloaders.ShippingMethodTranslationByIdAndLanguageCodeLoader
    ),
    site_models.SiteSettings: (
        dataloaders.SiteSettingsTranslationByIdAndLanguageCodeLoader
    ),
    discount_models.Voucher: (dataloaders.VoucherTranslationByIdAndLanguageCodeLoader),
}


def resolve_translation(instance, info, language_code):
    """Get translation object from instance based on language code."""

    loader = TYPE_TO_TRANSLATION_LOADER_MAP.get(type(instance))
    if loader:
        return loader(info.context).load((instance.pk, language_code))
    raise TypeError(f"No dataloader found to {type(instance)}")


@traced_resolver
def resolve_shipping_methods(info):
    return shipping_models.ShippingMethod.objects.all()


@traced_resolver
def resolve_attribute_values(info):
    return attribute_models.AttributeValue.objects.all()


@traced_resolver
def resolve_products(_info):
    return product_models.Product.objects.all()


@traced_resolver
def resolve_product_variants(_info):
    return product_models.ProductVariant.objects.all()


@traced_resolver
def resolve_sales(_info):
    return discount_models.Sale.objects.all()


@traced_resolver
def resolve_vouchers(_info):
    return discount_models.Voucher.objects.all()


@traced_resolver
def resolve_collections(_info):
    return product_models.Collection.objects.all()
