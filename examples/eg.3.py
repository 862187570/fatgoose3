"""
@Description: How to use proxy and cookies
@Usage: 
@Author: xlomg
@Date: 2021/8/29 下午3:16
"""

from fatgoose3 import FatGoose

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

proxies = {
    'http': '127.0.0.1:6789'
}

g = FatGoose()
g.config.http_headers = {'user-agent': UA}
g.config.http_proxies = proxies
g.config.http_headers['cookie'] = 'bb_geo_info={"country":"HK","region":"Asia","fieldN":"cp"}|1630401938042; pxcts=3e8fbc20-04bd-11ec-8cd2-b3feeb40fb79; _pxvid=3e8e9ca4-04bd-11ec-8917-576c79444c71; _reg-csrf=s%3ASR7J68z_nbtjIVZHKZkaS2B8.GMAKXuiosdCaW15fwDiLF%2BKELfQrEQjmPxjbZc6Nh0I; _user-status=anonymous; agent_id=42c00fe3-a7c6-4fc7-817d-b8408683ad09; session_id=49ad7b47-d543-46af-b3d2-8eea1d0a64cc; session_key=941041c3381825d3821cee5e00003315ab40ef22; gatehouse_id=307e7059-3c1c-42fa-a6a7-fd3258495e6d; bb_geo_info={"countryCode":"HK","country":"HK","field_n":"cp","trackingRegion":"Asia","cacheExpiredTime":1630401938755,"region":"Asia","fieldN":"cp"}|1630401938755; _sp_krux=false; _sp_v1_uid=1:442:9c1d8270-dd33-4d91-bdf0-717556a6dc78; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXSGvrJYAB7rhbDrAAAA; _sp_v1_opt=1:; _sp_v1_csv=null; _sp_v1_lt=1:; ccpaUUID=eeb22a2f-37d2-4216-9b15-6939d9f56d76; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; bbgconsentstring=req1fun1pad1; _gcl_au=1.1.1471559377.1629797140; bdfpc=004.0618011914.1629797140495; _ga=GA1.2.1381061563.1629797142; _fbp=fb.1.1629797142113.1604849760; _rdt_uuid=1629797142167.d0934f60-09ad-4dbb-9e57-ddf07f6c8825; _scid=988ca44c-45bb-449a-b5a7-cc356e1d65ea; _cc_id=5df5e1609ed0920d07d459f0f0f0c5cc; _li_dcdm_c=.bloomberg.com; _lc2_fpi=b1166d620485--01fdvqnqcf5fje5zb1a57ra6y9; _sctr=1|1629734400000; trc_cookie_storage=taboola%2520global%253Auser-id%3Dd5a5f492-ef6c-4fe7-ba35-80eea07d6db4-tuct564d9ac; panoramaId_expiry=1630401975910; panoramaId=3b0a568e58737e94a4996b442b954945a702e8c220d6a76147bd12b84e677fee; _gid=GA1.2.1761810210.1630030612; bb-mini-player-viewed=true; __sppvid=88bd4d61-c2b2-4cb5-8364-d41e1fac087d; _parsely_visitor={%22id%22:%22pid=7f986ae5cfa02dc96e77de37a4221af7%22%2C%22session_count%22:8%2C%22last_session_ts%22:1630070749501}; kw.pv_session=2; _sp_id.3377=3024460b-5e07-452b-a1d4-3809a14c29af.1629797154.6.1630070758.1630052089.dd6c0ad0-7a27-4ebd-a61a-6a95c0b93ed5; _uetsid=d7ccfde006dc11ec947913a07a3316d2; _uetvid=1a32f6a0cffb11ebbd1189ad070ed2ad; _pxff_rf=1; _pxff_fp=1; _px3=b3a94ad338545d5c6fb11bf13a1af67ce50ad23933d4d268e355f832ec5bdded:pqzDpasuqmCAKNUSkda4HKVma0s6zRl8GTofMjKbqK5NqVmI92HA2dpDUsI7TMbeivZS9Sn5uYFCV8brTYBKEw==:1000:+n9iqbbK8dNSPAmdpmxUgJdYjr9JDibqbch/RMi+FkFjXWLwQi+Y7oW8hVMOKpkvDSvFYvo2sd0ZE5Po6JPjlkt9hBzT6VyChWeipQ/aC5IKSiSqGdXf26d8R6ZNqjADQQvyjBCdr1a72xBYxq9YAvHIlEZX8Q+6zND54b+I1z0=; _px2=eyJ0IjoxNjMwMDczODEzNDA4LCJ2IjoiM2U4ZTljYTQtMDRiZC0xMWVjLTg5MTctNTc2Yzc5NDQ0YzcxIiwidSI6ImJhYTI2OGYwLTA3NDAtMTFlYy04MzVkLTkzNDgxMDcxMTQ3YyIsImgiOiI0NTkxOWRjYTliOThkZjM2NjQwZTE1MjJkYzkxYWY3YTExYTBmZjUyNDA1ZmYyZmE1MmRhYmZhOGVhY2I1MTY4In0=; _reg-csrf-token=9tDNmMLv-XbkLgm-FXvgcThkYGhk0ilRUzMA; _last-refresh=2021-8-27%2014%3A11; _sp_v1_data=2:334565:1629797139:0:26:0:26:0:0:_:-1; consentUUID=368aeaa5-6870-4c08-bcb8-33df343899fe; _pxde=274b18718434974d119f2bb978440357ae3e773a68f59ced73483fc2415cbffa:eyJ0aW1lc3RhbXAiOjE2MzAwNzM1MjI3NjgsImZfa2IiOjAsImlwY19pZCI6W119'

news = g.extract(url='https://www.bloomberg.com/news/articles/2021-08-06/china-s-wild-summer-of-stock-market-shocks-a-timeline')

print(f'news.title: %s\n' % news.title)
print(f'news.author: %s\n' % news.authors)
print(f'news.publish_date: %s\n' % news.publish_date)
print(f'news.cleaned_text: %s\n' % news.cleaned_text)
print(f'news.infos: %s\n' % news.infos)
g.close()
