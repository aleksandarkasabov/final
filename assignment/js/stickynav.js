var navigation, yPos, button;
function yScroll(){
  navigation=document.getElementById('navigation');
  button=document.getElementById('button');
  yPos=window.pageYOffset;
  if(yPos>300){//setting border for the y position of the screen which when crossed, some parameters changed
    navigation.style.position="fixed";
    navigation.style.top="0px";
    navigation.style.backgroundColor="rgba(33,33,33,0.5)";
    
    
  }
  else{
    navigation.style.position="absolute";
    navigation.style.top="50vh";
    navigation.style.backgroundColor="rgba(0,0,0,0)";
    button.style.color="rgba(0,0,0,1)";
  }
}
window.addEventListener("scroll", yScroll);// add event listener for scrolling by y axis