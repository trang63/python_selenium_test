cd destination-repo
git config --global user.name "$GIT_NAME"
git config --global user.email "$GIT_EMAIL"
git add .
git commit -m "Upload Allure Report"
git push https://"$GIT_ACCESS_KEY"@github.com/"$GIT_NAME"/allure_report.git