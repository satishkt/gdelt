import groovy.io.FileType
import org.slf4j.Logger
import org.slf4j.LoggerFactory

//requires three variables

///use the shell (made available under variable fsh)


Logger logger = LoggerFactory.getLogger("Groovy Copy File Logger");


if (!fsh.test(inputDir)) {
    logger.info("Removed the input id r{}",inputDir)
    //fsh.mkdir(inputDir)
    //logger.info("created the input id r{}",inputDir)
    println "Copying files into input dir *******************************************" + localSourceDir
    localSourceDir.eachFile() { file ->
      //  logger.info("copy file  the input id r{}",file)
       // fsh.copyFromLocal(file, inputDir)

    }

    fsh.chmod(700, inputDir)
}


if (fsh.test(outputDir)) {
    fsh.rmr(outputDir)
}