var delta = 0;
var currentSlideIndex = 0;
var numSlides = 5;
var scrollThreshold = 50;
 
function elementScroll (e) {
 
	// --- Scrolling up ---
	if (e.originalEvent.detail < 0 || e.originalEvent.wheelDelta > 0) {	
 
		delta--;
 
		if ( Math.abs(delta) >= scrollThreshold) {

			prevSlide();
		}
	}
 
	// --- Scrolling down ---
	else {
 
		delta++;
 
		if (delta >= scrollThreshold) {
			nextSlide();
		}
	}
 
	// Prevent page from scrolling
	return false;
}
 
 
function showSlide() {
 
	delta = 0;

	$('.slide').each(function(i, slide) {
		$(slide).toggleClass('active', (i >= currentSlideIndex));
	});
 
}
 
 
function prevSlide() {
 
	currentSlideIndex--;
 
	if (currentSlideIndex < 0) {
		currentSlideIndex = 0;
	}
 
	showSlide();
}
 
function nextSlide() {
 
	currentSlideIndex++;
 
	if (currentSlideIndex > numSlides) { 
		currentSlideIndex = numSlides;
	}

	console.log(currentSlideIndex + " out of " + numSlides);
 
	showSlide();
}

var windowHeight = $( window ).height();
$('#who-slides').height( windowHeight );
 
$(window).on({
	'DOMMouseScroll mousewheel': elementScroll
});