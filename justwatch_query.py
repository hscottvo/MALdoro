from justwatch import JustWatch

def get_links(title):
    just_watch = JustWatch(country='US')

    results = just_watch.search_for_item(query=title)

    links = []
    for i in results['items'][0]['offers']:
        links.append(i['urls']['standard_web'])

    return list(set(links))

