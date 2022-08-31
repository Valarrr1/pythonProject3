# sadece win10toast içinden ToastNotifier ı çalıştırıcaz.

from win10toast import ToastNotifier

#toastNotifier classını çağırdık
toaster= ToastNotifier()

#bildirimin atıldığı kısım hangi zaman aralığında atması içinde duration var.
toaster.show_toast("Title","Message",duration=5)