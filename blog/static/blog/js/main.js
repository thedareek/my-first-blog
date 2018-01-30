/** 
 * ===================================================================
 * main js
 *
 * ------------------------------------------------------------------- 
 */ 



(function($) {

	"use strict";

	/*---------------------------------------------------- */
	/* Preloader
	------------------------------------------------------ */ 


	/*----------------------------------------------------*/
	/*	Sticky Navigation
	------------------------------------------------------*/
   $(window).on('scroll', function() {

		var y = $(window).scrollTop(),
		    topBar = $('.navbar');
		    var windowWidth = $(window).width();
     
	   if (y > 20) {
		   if(windowWidth > 992){
		   	 topBar.addClass('navbar-inverse');
		     topBar.removeClass('navbar-static-top');
		     topBar.addClass('navbar-fixed-top');
		   	}
		   	else {
		   		topBar.removeClass('navbar-static-top');
		   		topBar.addClass('navbar-inverse');
		   		topBar.addClass('navbar-fixed-top');
		   	}

	   }
      else {
	      if(windowWidth > 992){
	         topBar.removeClass('navbar-inverse');
	         topBar.removeClass('navbar-fixed-top');
	         topBar.addClass('navbar-static-top');
	     	}
	     else {
		   		topBar.removeClass('navbar-static-top');
		   		topBar.addClass('navbar-fixed-top');
		   		topBar.addClass('navbar-inverse');
		   	}
      }
    
	});
	
	/*-----------------------------------------------------*/
  	/* Mobile Menu
   ------------------------------------------------------ */  	

})(jQuery);