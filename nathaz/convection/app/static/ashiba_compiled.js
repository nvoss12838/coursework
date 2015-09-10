/* Compiled with Ashiba v0.0 */

$(window).load(function(){
  $("#btn_calculate").on("click",
    ashiba.eventHandlerFactory("btn_calculate", "click")
  );
  $("#btn_plot").on("click",
    ashiba.eventHandlerFactory("btn_plot", "click")
  );
});