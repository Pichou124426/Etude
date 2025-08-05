#Faire un dictionnaire 


articles = {
    "pommes" : 10 ,
    "bananes" : 5,
    "oranges" : 8,
    "poires" : 4,
    "abricots" : 6
}

def up_new_article (quantity) :
    article = input ("what is the name of your article? \n")
    articles[article] = quantity 


def edit_value (quantity) :
    article = input ("what is the name of the article with this new values? \n")
    articles[article] = quantity 


def all_articles() :
    for article,quantity in articles.items():
        print(f"Article:{article}, Quantité: {quantity}")

def delete_article (article):
    del articles[article]

def check_article (article):
    article in articles

def article_quantity_inferior(threshold):
    for article,quantity in artciles.item():
        if int(threshold) > quantity :
            print(f"{article} a plus que {quantity} dans le stock.")

print (up_new_article(10),edit_value(2),all_articles(),delete_article(pommes),check_article(bananes),article_quantity_inferior(5))

