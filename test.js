const txtStartDateRotation=""
ddlRotation.onchange = function chnageStartDate(){
  var today = new Date();
  var daysToAdd = ddlRotation[0];
  var result = today.setDate(today.getDate() + daysToAdd);
}

