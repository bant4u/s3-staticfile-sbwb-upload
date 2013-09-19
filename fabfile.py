from fabric.api import *

common_dir='/src/main/webapp'
def liferay_theme():
	liferay_theme_dir='liferay-themes/petunia-theme'+common_dir
	with lcd(liferay_theme_dir):
		local('s3cmd put --recursive css s3://sbw_qa_bucket/petunia-theme1/')



def liferay_portlet():
	portlet_name_list=['admindashboard-portlet','appmarketplace-portlet','manageorganization-portlet',
						'sbsignupflow-portlet','sbworkbenchnavigation-portlet',
						'transaction-portlet','wizard-portlet','workingcapital-portlet']

	print portlet_name_list[len(portlet_name_list)-1]
	for i in range(0,len(portlet_name_list)):
		liferay_portlet_dir='portlets/'+portlet_name_list[i]+common_dir
		with lcd(liferay_portlet_dir):
			print portlet_name_list[i]
			local('s3cmd put --recursive --exclude ./WEB-INF --include ./* s3://sbw_qa_bucket/'+portlet_name_list[i]+'/')
			
			
def full_theme():
	liferay_theme()
	liferay_portlet()
