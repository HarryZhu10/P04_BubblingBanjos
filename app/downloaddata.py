import gdown

curl = 'https://drive.google.com/file/d/1DXS_eqGG3AbR1IrdOcWiXc_qPTEbGFHf/view?usp=sharing'
aurl = 'https://drive.google.com/file/d/1HtKO8nK2daRjJm1U50pyUZt_SF0cFmQj/view?usp=sharing'
curl = 'https://drive.google.com/uc?id=' + curl.split('/')[-2]
aurl = 'https://drive.google.com/uc?id=' + aurl.split('/')[-2]

gdown.download(curl)
gdown.download(aurl)