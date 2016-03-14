(function(){
	"use strict";
	jQuery(function($){
		fluidvids.init({
			selector: 'iframe', // runs querySelectorAll()
			players: ['www.youtube.com', 'player.vimeo.com'] // players to support
		});

		fluidvids.apply();

		var goDark = $(".dark-logo").length > 0;
		var bodyElement = $("body");
		$( "#menu-toggle" ).click(function() {
			$("html").animate({ 
				scrollTop: 0
			});
			bodyElement.animate({ 
				scrollTop: 0
			}, {
				complete: function() {
					bodyElement.toggleClass( "menu-visible" );
					if (goDark){
						bodyElement.toggleClass( "dark-logo" );
					}
				}
			});
		});

		$(".work.project").click(function(){
			$(this).toggleClass("money");
		})

		var windowHeight = $( window ).height();
		$('#index-hero').height( windowHeight - 25 );
		$('#detail-hero').height( windowHeight * .55 );
		$('.where-map').height( windowHeight - 40 );
		$('.fourohfour').height( windowHeight );
		$('.pig-pen').height( windowHeight );
		$('.monety').height( windowHeight );
		$('.page-content').css('min-height', windowHeight - 292);

	});

	[].slice.call( document.querySelectorAll( '.si-icons-default > .si-icon' ) ).forEach( function( el ) {
        var svgicon = new svgIcon( el, svgIconConfig );
    } );

    if (typeof addthis !== 'undefined') {
	    addthis.layers({
			'theme' : 'transparent',
			'share' : {
			  'position' : 'left',
			  'numPreferredServices' : 5
			}, 
			'follow' : {
			  'services' : [
			    {'service': 'twitter', 'id': 'ahochoy'},
			    {'service': 'linkedin', 'id': 'ahochoy'},
			    {'service': 'google_follow', 'id': '+AndrewHoChoy'},
			    {'service': 'instagram', 'id': 'ahochoy'},
			    {'service': 'tumblr', 'id': 'ahochoy'}
			  ]
			}
		});
	}

	if(!document.createTouch) {
    	var s = skrollr.init();
	}

    /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
    var disqus_shortname = 'ahochoy'; // required: replace example with your forum shortname

    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function () {
        var d = document.createElement('script'); d.async = true;
        d.type = 'text/javascript';
        d.src = '//' + disqus_shortname + '.disqus.com/count.js';
        (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(d);
    }());
})();