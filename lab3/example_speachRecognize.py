import speach_recognize

#这里需要申请讯飞API ，并进行防火墙配置
#每个免费账户有每天500次限制
sr = speach_recognize.speachRecognizer(accountList = [{'APPID':'5cad4c88','API_KEY':'55dba8b5606fac7572450e79a2f03bcc'}])
sr.setAudiFile('audio.wav')
print(sr.getResponse())
