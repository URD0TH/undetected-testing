"""Bypass bot-detection to view SocialBlade ranks for YouTube"""
from seleniumbase import SB

with SB(uc=True, test=True, ad_block=True, pls="none") as sb:
    url = "https://socialblade.com/youtube/channel/UCSQElO8vQmNPuTgdd83BHdw"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    sb.uc_gui_click_captcha()
    sb.sleep(1.5)
    sb.cdp.remove_elements("#lngtd-top-sticky")
    sb.sleep(1.5)
    name = sb.cdp.get_text("h1")
    source = sb.get_page_source()
    base = "https://www.youtube.com/c/"
    base2 = 'href="/youtube/c/'
    start = source.find(base2) + len(base2)
    end = source.find('"', start)
    link = base + source[start:end]
    print("********** SocialBlade Stats for %s: **********" % name)
    print(">>> (Link: %s) <<<" % link)
    print(sb.get_text('[class*="grid lg:hidden"]'))
    print("********** SocialBlade Ranks: **********")
    print(sb.get_text('[class*="gap-3 flex-1"]'))
    for i in range(17):
        sb.cdp.scroll_down(6)
        sb.sleep(0.1)
    sb.sleep(2)
