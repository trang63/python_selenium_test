cd destination-repo
git config --global user.name "${{ secrets.GIT_NAME }}"
git config --global user.email "${{ secrets.GIT_EMAIL }}"
git add .
git commit -m "Upload Allure Report"
git push https://${{ secrets.ACCESS_KEY }}@github.com/${{ secrets.GIT_NAME }}/allure_report.git