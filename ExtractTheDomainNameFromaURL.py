def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]