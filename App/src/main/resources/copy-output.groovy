/**
 * Created by Satish on 4/18/16.
 */
//requires three variables

///use the shell (made available under variable fsh)
if(fsh.test(outputDir)){
    println "Copying to Local ****************************."
    fsh.copyToLocal(outputDir,localOutputDir)
}