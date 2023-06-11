import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler, BlockElementHandler
from wagtail import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import SiteElement

@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):
    """
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block type,
    and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = 'blockquote'
    type_ = 'blockquote'
    tag = 'blockquote'

    control = {
        'type': type_,
        'label': '❝',
        'description': 'Blockquote',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'blockquote',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {tag: BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: tag}},
    })


@hooks.register('register_rich_text_features')
def register_strikethrough_feature(features):
    feature_name = 'strikethrough'
    type_ = 'STRIKETHROUGH'
    tag = 's'

    control = {
        'type': type_,
        'label': 'S',
        'description': 'Strikethrough',
        # 'style': {'textDecoration': 'line-through'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.default_features.append('strikethrough')


@hooks.register('register_rich_text_features')
def register_align_right_feature(features):
    feature_name = 'alignright'
    type_ = 'ALIGNRIGHT'
    tag = 'div'

    control = {
        'type': type_,
        'label': 'AR',
        'description': 'Align Right',
        'style': {'textAlign': 'right'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.default_features.append('alignright')


class SiteElementModelAdmin(ModelAdmin):
    model = SiteElement
    menu_label = 'Site Elements'
    list_display = ('name', 'key', 'value')


modeladmin_register(SiteElementModelAdmin)
