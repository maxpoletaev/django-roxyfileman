function previewFile(){
  var f = getSelectedFile();
  if(f){
    window.open(RoxyFilemanConf.RETURN_URL_PREFIX + f.fullPath.slice(1));
  }
}
