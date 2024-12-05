# Ghibli wallpaper downloader

A very simple script to download wallpapers from the Ghibli's collection.

More info from Studio Ghibli: 

* [News 18/09/2020](https://www.ghibli.jp/info/013344/)
* [News 18/12/2020](https://www.ghibli.jp/info/013409/)
* [News 04/08/2023](https://www.ghibli.jp/info/013762/)
* [News 18/08/2023](https://www.ghibli.jp/info/013772/)

* [Web conference wallpapers 03/02/2022](https://www.ghibli.jp/info/013251/)

## This tool

From terminal, just run command:
```bash
python downloader.py 
```

Less than 3 minutes to download 1178 wallpapers (~321 mb).
Internet connection dependent.


## Limits

* It doesn't handle errors. But if you run it more than once, it just downloads the missing images.
* It's possible increase parallelism, using more threads.
* It download images in the current directory.
