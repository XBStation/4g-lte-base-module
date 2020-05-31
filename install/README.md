Each of these shield can be connected to Internet via PPP(Point to Point Protocol).

Without further ado let us jump into the installation process:

Clone the repository

`git clone https://github.com/XBStation/4g-lte-base-module.git` 

Now change the permission of the downloaded script.

```
cd 4g-lte-base-module/install
chmod +x install.sh
```

Now install the script

`sudo ./install.sh`
  
It will ask several questions, just answer them accordingly to complete the installation process. The questions are: 

`What is your carrier APN?`

Here, it asks for your carrier's APN. For me it is hologram. 

`Does your carrier need username and password? [Y/n]`

Then it asks if your carrier needs username and password. 

`Enter username`
If yes then it will ask for user name.

`Enter password`
Then it will ask for password. 

`Do you want to activate auto connect/reconnect service at R.Pi boot up?`

This option allows you to connect to Internet via your shield automatically when your Raspberry Pi Starts. If you want to connect to Internet automatically type Y else n. If you have selected n then you will need to run `sudo pon` to connect to internet and `sudo poff` to stop it. 

Enjoy your Internet connection.

## License

MIT. Copyright (c) [Sixfab](https://github.com/sixfab/Sixfab_PPP_Installer/tree/master/ppp_installer).
