"""shopping_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from site_admin import views as admin_view
from Buyer import views as Buyer_view
from seller import views as seller_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',admin_view.index,name='index'),
    url(r'^buyerRegistration/$',Buyer_view.buyerRegistration,name='buyerRegistration'),
    url(r'^registerAction/$',Buyer_view. registerAction,name='registerAction'),
    url(r'^sellerRegistration/$',seller_view.sellerRegistration,name='sellerRegistration'),
    url(r'^sellerregisterAction/$',seller_view.sellerregisterAction,name='sellerregisterAction'),
    url(r'^login/$',admin_view.login,name='login'),
    url(r'^loginAction/$',admin_view.loginAction,name='loginAction'),
    url(r'^viewAllSellers/$',admin_view.viewAllSellers,name='viewAllSellers'),
    url(r'^updateProfile/$',Buyer_view.updateProfile,name='updateProfile'),
    url(r'^updateBuyerAction/$',Buyer_view.updateBuyerAction,name="updateBuyerAction"),
    url(r'^addCategory/$',admin_view.addCategory,name='addCategory'),
    url(r'^addCategoryAction/$',admin_view.addCategoryAction,name='addCategoryAction'),
    url(r'^checkUsername/$',Buyer_view.checkUsername,name='checkUsername'),
    url(r'^approve/(?P<uid>\d+)/$',admin_view.approve,name='approve'),
    url(r'^reject/(?P<uid>\d+)/$',admin_view.reject,name='reject'),
    url(r'^addProduct/$',seller_view.addProduct,name='addProduct'),
    url(r'^addProductAction/$',seller_view.addProductAction,name='addProductAction'),
    url(r'^viewProduct/$',seller_view.viewProduct,name='viewProduct'),
    url(r'^delete/(?P<uid>\d+)/$',seller_view.delete,name='delete'),
    url(r'^edit/(?P<uid>\d+)/$',seller_view.edit,name='edit'),
    url(r'^editAction/$',seller_view.editAction,name='editAction'),
    url(r'^updateSeller/$',seller_view.updateSeller,name='updateSeller'),
    url(r'^updateSellerAction/$',seller_view.updateSellerAction,name='updateSellerAction'),
    url(r'^viewAllProduct/$',Buyer_view.viewAllProduct,name='viewAllProduct'),
    url(r'^addtocart/(?P<uid>\d+)/$',Buyer_view.addtocart,name='addtocart'),
    url(r'^addtoCartAction/$',Buyer_view.addtoCartAction,name='addtoCartAction'),
    url(r'^viewCart/$',Buyer_view.viewCart,name='viewCart'),
    url(r'^delet/(?P<uid>\d+)/$',Buyer_view.delet,name='delet'),
    url(r'^orderAction/$',Buyer_view.orderAction,name='orderAction'),
    url(r'^viewOrder/$',Buyer_view.viewOrder,name='viewOrder'),
    url(r'^cancel/(?P<uid>\d+)/$',Buyer_view.cancel,name='cancel'),
    url(r'^customerOrderView',seller_view.customerOrderView,name='customerOrderView'),
    url(r'^accept/(?P<uid>\d+)/$',seller_view.accept,name='accept'),
    url(r'^reject1/(?P<uid>\d+)/$',seller_view.reject1,name='reject1'),
    url(r'^conformCancel/(?P<uid>\d+)/$',seller_view.conformCancel,name='conformCancel'),
    url(r'^trackOrder/(?P<uid>\d+)/$',seller_view.trackOrder,name='trackOrder'),
    url(r'^trackOrderAction/$',seller_view.trackOrderAction,name='trackOrderAction'),
    url(r'^viewTrackDetails/(?P<uid>\d+)/$',Buyer_view.viewTrackDetails,name='viewTrackDetails'),
    url(r'^searchProduct/$',Buyer_view.searchProduct,name='searchProduct'),
    url(r'^searchProductAction/$',Buyer_view.searchProductAction,name='searchProductAction'),
    url(r'^searchProductCategory/$',Buyer_view.searchProductCategory,name='searchProductCategory'),
    url(r'^searchProductbyCategoryAction/$',Buyer_view.searchProductbyCategoryAction,name='searchProductbyCategoryAction'),
    url(r'^logout/$',admin_view.logout,name='logout'),
    url(r'^forgotPassword/$',admin_view.forgotPassword,name='forgotPassword'),
    url(r'^forgotPasswordUsernameCheck/$',admin_view.forgotPasswordUsernameCheck,name='forgotPasswordUsernameCheck'),
    url(r'^forgotPasswordDOBPhoneCountrycheck/$',admin_view.forgotPasswordDOBPhoneCountrycheck,name='forgotPasswordDOBPhoneCountrycheck'),
    url(r'^newpasswordAction/$',admin_view.newpasswordAction,name='newpasswordAction'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
