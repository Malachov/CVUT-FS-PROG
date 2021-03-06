import os
import datetime as dt
import pandas as pd
import email_module
import schedule
import time


def check_data():
    # nastaveni pozadovanych limitnich hodnot
    max_nastavene = 26
    min_nastavene = 16

    now = dt.datetime.now()
    ago = now - dt.timedelta(days=1)
    dff = pd.DataFrame()
    historical_data = pd.read_csv("historical_data.csv")
    historical_data.set_index("id", drop=True, inplace=True)

    # prohledavani slozky data pro soubory stare maximalne 1 den
    for root, dirs, files in os.walk("data"):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print("%s modified %s" % (path, mtime))
                df = pd.read_csv(path, index_col=None, header=0)
                dff = dff.append(df, ignore_index=True)  # pripisovani dovych souboru do spolecneho dataframe

    dff.set_index("id", drop=True, inplace=True)
    dff.to_csv("data/analyze.csv")

    maximum = dff["teplota"].max()
    minimum = dff["teplota"].min()

    # vytvoreni dataframe z hodnot, ktere se nachazeji mimo zadany interval
    dff_max_alert = dff[dff.teplota > max_nastavene]
    dff_min_alert = dff[dff.teplota < min_nastavene]

    # odesilani emailu
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    send_to = "ondrejsalva@gmail.com"
    mail_subject = "Zavada na lince"

    email_message = f"""
    Dobry den,

    kontrolovane hodnoty na vyrobni lince presahly maximalni povolene hodnoty v techto pripadech:

    {dff_max_alert}

    Naopak hodnoty nizsi nez dovolene minimum byly namereny v techto pripadech:
    {dff_min_alert}

    Prosime o kontrolu linky
    """

    # podminka pro odeslani emailu
    if maximum > max_nastavene or minimum < min_nastavene:
        email_module.send_email(sender, password, send_to, mail_subject, email_message)
    else:
        pass

    # sdruzovani chybovych hodnot do dataframe

    historical_data = historical_data.append(dff_max_alert)
    historical_data = historical_data.append(dff_min_alert)

    historical_data.to_csv("historical_data.csv")


if __name__ == "__main__":
    # schedule.every(1).minutes.do(check_data)
    schedule.every().day.at("10:30").do(check_data)

    while 1:
        schedule.run_pending()
        time.sleep(1)
