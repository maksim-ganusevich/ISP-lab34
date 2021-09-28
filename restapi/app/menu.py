def main_menu():
    return {
        "reply_markup": {"inline_keyboard": [[{"text": "Business", "callback_data": "BusinessMenu"},
                                              {"text": "Info", "callback_data": "InfoMenu"}],
                                             [{"text": "Balance", "callback_data": "BalanceMenu"},
                                              {"text": "Admin", "callback_data": "AdminMenu"}]]}}


def business_menu():
    return {
        "reply_markup": {"inline_keyboard": [[{"text": "Balance", "callback_data": "BalanceMenu"},
                                              {"text": "BuyCompany", "callback_data": "BuyCompany"}],
                                             [{"text": "BuyFabric", "callback_data": "BuyFabric"},
                                              {"text": "BuyMonopoly", "callback_data": "BuyMonopoly"}],
                                             [{"text": "BuyStockExchange", "callback_data": "BuyStockExchange"},
                                              {"text": "Back", "callback_data": "BackMenu"}]]}}


def admin_menu():
    return {
        "reply_markup": {"inline_keyboard": [[{"text": "Back", "callback_data": "BackMenu"},
                                              {"text": "Info", "callback_data": "AdminInfo"}],
                                             [{"text": "ChangeBalance", "callback_data": "ChangeBalance"},
                                              {"text": "DeleteUser", "callback_data": "DeleteUser"}]]}}
