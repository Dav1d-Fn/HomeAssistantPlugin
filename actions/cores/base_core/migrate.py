from HomeAssistantPlugin.actions import const
from HomeAssistantPlugin.actions.cores.customization_core import customization_const
from HomeAssistantPlugin.actions.show_icon import icon_const
from HomeAssistantPlugin.actions.show_icon.icon_settings import ShowIconSettings


def migrate(action) -> None:
    settings = action.get_settings()

    if settings.get(const.SETTING_VERSION, 0) > 1:
        return

    migrate_v1_v2(action)

def migrate_v1_v2(action) -> None:
    settings = action.get_settings()

    settings[const.SETTING_VERSION] = 2
    action.set_settings(settings)

    if action.__class__.__name__ != "ShowIcon":
        return

    settings[icon_const.SETTING_ICON][icon_const.SETTING_IMAGE] = icon_const.EMPTY_STRING
    for customization in settings[icon_const.SETTING_ICON][customization_const.SETTING_CUSTOMIZATIONS]:
        customization[icon_const.CUSTOM_IMAGE] = icon_const.EMPTY_STRING

    action.set_settings(settings)