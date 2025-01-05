import subprocess

def get_saved_wifi_passwords():
    # تشغيل الأمر لمعرفة الشبكات المحفوظة
    networks_data = subprocess.check_output("netsh wlan show profiles", shell=True, encoding='utf-8')
    networks = [line.split(":")[1].strip() for line in networks_data.split("\n") if "All User Profile" in line]

    wifi_passwords = {}
    for network in networks:
        try:
            # الحصول على تفاصيل الشبكة وكلمة المرور
            profile_data = subprocess.check_output(f"netsh wlan show profile \"{network}\" key=clear", shell=True, encoding='utf-8')
            for line in profile_data.split("\n"):
                if "Key Content" in line:
                    wifi_passwords[network] = line.split(":")[1].strip()
                    break
            else:
                wifi_passwords[network] = "No password found"
        except subprocess.CalledProcessError:
            wifi_passwords[network] = "Error reading profile"

    return wifi_passwords

# عرض النتائج
passwords = get_saved_wifi_passwords()
for network, password in passwords.items():
    print(f"Network: {network}, Password: {password}")