from flask_restful import Resource
from flask import request
from app.menu import *
from multiprocessing import Process
import json
import logging


logging.basicConfig(level="INFO", filename="log.log")
logger = logging.getLogger(__name__)



class RestApi(Resource):

    def get(self, id):
        p = Process(target=logger.info(f'Get method initialized'))
        if "BusinessMenu" in id:
            p = Process(target=logger.info("BusinessMenu was returned"))
            chat_data = business_menu()
            chat_data = json.dumps(chat_data)
            return chat_data, 200
        elif "BackMenu" in id:
            p = Process(target=logger.info("BackMenu was returned"))
            chat_data = main_menu()
            chat_data = json.dumps(chat_data)
            return chat_data, 200
        elif "Menu" in id:
            p = Process(target=logger.info("Bad request"))
            return "Bad request. You must send Menu type", 400
        else:
            p = Process(target=logger.info("Bad request"))
            return "Menu not found or message was invalid", 404

    def post(self, id=0):
        from app.database_models  import Users, Business, db, Company, Fabric, Monopoly, AchievementManager, StockExchange, Medals, BusinessInfo
        p = Process(target=logger.info("Post request initiated"))
        chat_data = "Chat info"
        if "callback_query" in request.json:
            user_id = request.json["callback_query"]["from"]["id"]
            rdata = request.json["callback_query"]["data"]
            try:
                user = Users.query.get(int(user_id))
                if rdata == "BalanceMenu":
                    p = Process(target=logger.info("Balance was returned"))
                    balance = user.balance
                    chat_data = json.dumps(f"User balance: {balance} dogcoins")
                    return chat_data, 200
                elif rdata == "AdminMenu" and user.is_admin == 1:
                    p = Process(target=logger.info("AdminMenu was returned"))
                    chat_data = json.dumps(admin_menu())
                    return chat_data, 200
                elif rdata == "BuyCompany":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy company"))
                    business_id = user.business_id
                    business = Business.query.get(int(business_id))
                    company = Company.query.get(int(business.company_id))
                    if company.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought company"))
                        user.balance -= company.price
                        company.count += 1
                        chat_data = json.dumps("Company was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for company(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "BuyFabric":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy fabric"))
                    business_id = user.business_id
                    business = Business.query.get(int(business_id))
                    fabric = Fabric.query.get(int(business.fabric_id))
                    if fabric.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought fabric"))
                        user.balance -= fabric.price
                        fabric.count += 1
                        chat_data = json.dumps("Fabric was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for fabric(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "BuyStockExchange":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy extange"))
                    business_id = user.business_id
                    business = Business.query.get(int(business_id))
                    stock = StockExchange.query.get(int(business.stockexchange_id))
                    if stock.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought exchange"))
                        user.balance -= stock.price
                        stock.count += 1
                        chat_data = json.dumps("Stock was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for stock(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "BuyMonopoly":
                    p = Process(target=logger.info(f"User: {user_id} is trying to buy monopoly"))
                    business_id = user.business_id
                    business = Business.query.get(int(business_id))
                    monopoly = Monopoly.query.get(int(business.monopoly_id))
                    if monopoly.price <= user.balance:
                        p = Process(target=logger.info(f"User: {user_id} bought monopoly"))
                        user.balance -= monopoly.price
                        monopoly.count += 1
                        chat_data = json.dumps("Monopoly was bought!")
                    else:
                        chat_data = json.dumps("Not enough money for monopoly(")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "AdminInfo":
                    p = Process(target=logger.info(f"Admin info was returned"))
                    users = Users.query.all()
                    medals = Medals.query.all()
                    achievements = AchievementManager.query.all()
                    text = ""
                    for user in users:
                        for medal in medals:
                            for achievement in achievements:
                                if achievement.user_id == user.id and achievement.medal_id == medal.id:
                                    text += f"User: {user.username} has {medal.medal_type} achievement!"
                    chat_data = json.dumps(text)
                    return chat_data, 200
                elif rdata == "ChangeBalance":
                    p = Process(target=logger.info(f"User: {user_id} get 100 dogcoins from admin panel"))
                    user.balance += 100
                    chat_data = json.dumps("This action will recharge your balance with 100 dogcoins")
                    db.session.commit()
                    return chat_data, 200
                elif rdata == "InfoMenu":
                    p = Process(target=logger.info(f"Info menu was returned"))
                    text = ""
                    business_id = user.business_id
                    business = Business.query.get(int(business_id))
                    company = Company.query.get(int(business.company_id))
                    text += f"Amount of companys: {company.count}. Price per item:{int(company.price)} dogcoins"
                    fabric = Fabric.query.get(int(business.fabric_id))
                    text += f"Amount of fabrics: {fabric.count}. Price per item:{int(fabric.price)} dogcoins"
                    monopoly = Monopoly.query.get(int(business.monopoly_id))
                    text += f"Amount of monopolys: {monopoly.count}. Price per item: {int(monopoly.price)}$"
                    stockExchange = StockExchange.query.get(int(business.stockexchange_id))
                    text += f"Amount of Stocks: {stockExchange.count}. Price per item: {int(stockExchange.price)}$"
                    chat_data = json.dumps(text)
                    return chat_data, 200
                db.session.commit()
            except (RuntimeError, TypeError, NameError, AttributeError):
                chat_data = json.dumps("Error occurred while processing menu operations or buy operations")
                return chat_data, 200
        elif "message" in request.json and "text" in request.json["message"]:
            user_id = request.json["message"]["from"]["id"]
            username = request.json["message"]["from"]["username"]
            user = Users.query.get(int(user_id))
            if user is None and request.json["message"]["text"] == "/start":
                p = Process(target=logger.info(f"User: {user_id} is starting application"))
                medal = Medals.query.get(int(1))
                if medal is None:
                    medal = Medals(medal_type="New player", id=1)
                    db.session.add(medal)
                    db.session.commit()
                    new_medal = Medals(medal_type="10000 dogcoins!", id=2)
                    db.session.add(new_medal)
                    db.session.commit()
                    another_medal = Medals(medal_type="100000 dogcoins! Great player!", id=3)
                    db.session.add(another_medal)
                    db.session.commit()
                stock = StockExchange(price=2500, income=200, count=0)
                fabric = Fabric(price=100, income=5, count=0)
                monopoly = Monopoly(price=1000, income=75, count=0)
                company = Company(price=25, income=1, count=0)
                db.session.add(stock)
                db.session.add(fabric)
                db.session.add(monopoly)
                db.session.add(company)
                db.session.commit()
                business = Business(company_id=company.id, fabric_id=fabric.id, monopoly_id=monopoly.id, stockexchange_id=stock.id)
                db.session.add(business)
                db.session.commit()
                b_info = BusinessInfo(business_id=business.id, info="Normal")
                db.session.add(b_info)
                db.session.commit()
                user = Users(id=int(user_id), balance=50, username=username, is_admin=1, business_id=business.id)
                db.session.add(user)
                db.session.commit()
                achive_manager = AchievementManager(medal_id=1, user_id=int(user_id))
                db.session.add(achive_manager)
                db.session.commit()
                chat_data = main_menu()
                chat_data = json.dumps(chat_data)
                return chat_data, 200
            else:
                chat_data = main_menu()
                chat_data = json.dumps(chat_data)
                return chat_data, 200
        chat_data = "Error request!"
        chat_data = json.dumps(chat_data)
        return chat_data, 200

    def put(self, id=0):
        from app.database_models import Users, Business, db, Company, Fabric, Monopoly, AchievementManager, StockExchange, Medals, BusinessInfo
        users = Users.query.all()
        p = Process(target=logger.info(f"Users are getting income from their army's"))
        for user in users:
            business = Business.query.get(int(user.business_id))
            company = Company.query.get(int(business.company_id))
            fabric = Fabric.query.get(int(business.fabric_id))
            monopoly = Monopoly.query.get(int(business.monopoly_id))
            stock = StockExchange.query.get(int(business.monopoly_id))
            user.balance += company.count * company.income
            user.balance += fabric.count * fabric.income
            user.balance += monopoly.count * monopoly.income
            user.balance += stock.count * stock.income
            db.session.commit()
        return 200

    def delete(self, id):
        from app.database_models import Users, Business, db, Company, Fabric, Monopoly, AchievementManager, StockExchange, Medals, BusinessInfo
        user = Users.query.get(id)
        business = Business.query.get(int(user.business_id))
        BusinessInfo.query.filter_by(business_id=business.id).delete()
        AchievementManager.query.filter_by(user_id=id).delete()
        Users.query.filter_by(id=id).delete()
        Business.query.filter_by(id=user.business_id).delete()
        Company.query.filter_by(id=business.company_id)
        Fabric.query.filter_by(id=business.fabric_id)
        Monopoly.query.filter_by(id=business.monopoly_id)
        StockExchange.query.filter_by(id=business.monopoly_id)
        db.session.commit()
        p = Process(target=logger.info(f"User: {user.id} has deleted his account!"))
        return "User was deleted, if he exist", 200

