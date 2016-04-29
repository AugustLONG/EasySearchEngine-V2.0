name := "InvertedIndexBuilder"
 
version := "1.0"
  
scalaVersion := "2.10.4"
libraryDependencies += "org.apache.spark" % "spark-core_2.10" % "1.4.0"

mergeStrategy in assembly <<= (mergeStrategy in assembly) { mergeStrategy => {
    case entry => {
      val strategy = mergeStrategy(entry)
      if (strategy == MergeStrategy.deduplicate) MergeStrategy.first
      else strategy
    }
  }
}
