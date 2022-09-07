import os
def LogExplanation(Message,HSMCommand):
    Firt_Header = Message[1:9]
    Second_Header = Message[11:25]
    if Firt_Header == 'ProCrypt':
        First_Message = "Standart HSM Mesajıdır."
        Second_Head = ProCryptDef(Second_Header)
        return_Message = str(First_Message) +" "+ str(Second_Head)
        return return_Message
    elif Firt_Header == 'commands':
        First_Message = "HSM Komutu Çalışmaktadır."
        Second_Head = commandsDef(Second_Header)
        return_Message = First_Message +" "+ Second_Head
        return return_Message
    else:
        pass
def ProCryptDef(Second_Header):
    PSecond = str(Second_Header)
    global ProCryptMessage
    if PSecond == 'commandHandler':
        ProCryptDef = 'Handler çalışmaktadır'
    elif PSecond == 'logout@2380]':
        ProCryptDef = 'Çıkış Yapıldı'
    elif PSecond == 'start@1329]':
        ProCryptDef = 'Başlıyor....'
    return ProCryptDef

def commandsDef(Second_Header):
    Second = str(Second_Header)
#    print(Second)
    global CommandMessage
    if Second == 'commandHandler.':
        CommandMessage = 'Standart Bir Mesajdır.'
    elif Second == 'C_GetSlotList:':
        CommandMessage = 'HSM içerinde bulunan Slotlar listelenir.'
    elif Second == 'C_GetSlotInfo:':
        CommandMessage = 'Slot Bilgisi Çekilmiştir.'
    elif Second == 'C_GetTokenInfo':
        CommandMessage = 'Token Bilgiler Çekilmiştir.'
    elif Second == 'C_InitToken::e':
        CommandMessage = 'Yeni Bir Token Oluşturuldu.'
    elif Second == 'C_OpenSession:':
        CommandMessage = 'Yeni bir Sessions açıldı.'
    elif Second == 'C_Login::execu':
        CommandMessage = 'Login işlemi gerçekleştirildi.'
    elif Second == 'C_InitPIN::exe':
        CommandMessage = 'Yeni bir PIN belirlendi.'
    elif Second == 'C_CloseSession':
        CommandMessage = 'Açık olan session kapatıldı.'
    else:
        CommandMessage = 'Henüz Belirlenmedi.'
    return CommandMessage
