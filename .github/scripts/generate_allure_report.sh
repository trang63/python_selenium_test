mkdir reports/history
cp -R destination-repo/allure-history/* reports/history
allure generate reports -o reports_allure
sudo systemsetup -settimezone "Asia/Ho_Chi_Minh"
current_date=$(date +%Y-%m-%d)
current_time=$(date +%H-%M-%S)
folder_name="report_${current_date}_${current_time}"
mkdir "destination-repo/$folder_name"
cp -R ./reports_allure/* "destination-repo/$folder_name"
echo "folder_name=$folder_name" >> $GITHUB_ENV
echo "current_datetime=$(date +'%Y-%m-%d %H:%M:%S (%Z)')" >> $GITHUB_ENV
echo "QUESTION=$1" >> $GITHUB_ENV
if [ "$1" = "success" ]; then
echo "color=#36a64f" >> $GITHUB_ENV
echo "test_status=Pass" >> $GITHUB_ENV
else
echo "color=#ff0000" >> $GITHUB_ENV
echo "test_status=Fail" >> $GITHUB_ENV
fi
