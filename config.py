HEADERS = {
    'authority': 'www.linkedin.com',
    'method': 'GET',
    'path': '/jobs/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8,gu;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

COOKIE = {
    "li_sugr": "7d4895c4-83e1-4f4a-9626-d421ce925753",
    "AnalyticsSyncHistory": "AQJZcTAeTurgfAAAAZKcPbN6VbWuQGqLrXx5E8N1B_PimjF_tyZ3K2-VaovjfEYrXlL9-jSWO8DaKek3HQwDTw",
    "timezone": "America/Toronto",
    "bcookie": '"v=2&e20bd5fd-727d-46d6-8f26-b353baf1cc6a"',
    "bscookie": '"v=1&20241017204902baf746c7-64c0-47fe-874e-43ed55b7d65aAQFxKjfubMSb6_BlOWZgflLFf2XRZGf6"',
    "dfpfpt": "2a7371fead724d48a4cf75ba00de7acb",
    "li_rm": "AQE6A1qkSpCFdgAAAZKraljAYWa8QmMqdxqIYEUsnmW43eF98s5Au2HZQhHN80YkI_RkCCNz_6KPHj2oEqUYYONwSpWSYHUwsr4Eu6PDehxB3MXQisszcRFK",
    "visit": "v=1&M",
    "g_state": '{"i_l":1,"i_p":1729459939265}',
    "li_theme_set": "user",
    "li_theme": "dark",
    "liap": "true",
    "li_at": "AQEDAUoX_LMAxtDcAAABkraBTbsAAAGS2o3Ru1YAGxMi2AarecLirDM6re1Zv7ka-wAvaEA7u9I2pzN_HopP4QsaAbsDtxNGxmEFlvlaI8pW5LEJ2izb3OqjTV2XvTVydzU_P6hS56UGZhIh7lt1qqpa",
    "fptctx2": "taBcrIH61PuCVH7eNCyH0LNKRXFdWqLJ6b8ywJyet7WmdqUjKGnwKULJH0tEgmswjg%252fWkbEfPTix%252bKXrH3gwdZJ1YyoThrKdenkcl8GcrT8zXtS7fX1mDz97FZ4uo73DZ0MBnslH2uBE9DKZuY8zTSj5EqGnjbxSpLBdLrtNfnuoAnozsLVyfml%252fiC22Nd0ZDVVb9jgO9ezGznrsBHlJoecobzU4nrIRHmd%252fSVgJZ7rWHLzuqovlKe1j6FUfZjrj%252f7tnJhge%252fcWfSbzs9SkoVjr8WYHdxBnWttaE7V7b4xdWXhqHn%252fSxmZ3%252fSEMqSmQ8x6Bnbzfjy0tAFJuHeYg63%252b08y66X8Sbrd27ldqzRlvU%253d",
    "UserMatchHistory": "AQKfkU2tQRvIqgAAAZLUMVwlfPDzp1dCtFTSlIB97yuVQzY4NTxZxxKE_3zF5cLA6alh-zZoXxvELsvO5so6sKw4HQVqQDdJe6bql4cEoV1LOD-c7WoOSJzC94Yt2REDypU_w51FtYr1SDT4TABztPKDyRIOIGn2wnAtG7qBP8ngrOOIPRets6zf3fDhDnIQfN9tcvLzdfz_l5c514ZXovjrPjSkma48wt35KYDfmnJaTTTeklYSZyTb8XY2vkCArOR8sd9t_yEXTiUsBHm2VYpRSYGv3uiRNeOwvKEbOhsA3QA7eMNkplh3pbRJXFYCkmhXCvT7ooHiwn2Ix6ldxqyFY5VoPO8p1byTGa-x0izEu7Fb5w"
}



# https://www.linkedin.com/jobs/search?keywords=Project%20Management&location=Canada&currentJobId=


job_posting_url = 'https://www.linkedin.com/jobs/search?keywords='
# https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Ftrk%3Dorganization_guest_guest_nav_menu_jobs%26position%3D1%26pageNum%3D0%26original_referer%3D&position=1&pageNum=0
BASE_URL = 'https://www.linkedin.com/jobs/search?keywords='
INFO_CONTAINER_DIV = 'base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card'
JOB_CLASS_CONTAINER_UL = 'jobs-search__results-list'
