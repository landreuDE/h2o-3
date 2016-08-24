package water.parser;

import org.junit.Assume;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.util.Set;
import java.util.TreeSet;

import water.TestUtil;
import water.fvec.Frame;
import water.util.Log;

import static org.junit.Assert.assertEquals;
import static water.parser.OrcTestUtils.compareH2OFrame;

/**
 * Test suite for orc parser.
 *
 * This test will build a H2O frame for all orc files found in smalldata/parser/orc directory
 * and compare the H2O frame content with the orc file content read with Core Java commands.
 * Test is declared a success if the content of H2O frame is the same as the contents read
 * by using core Java commands off the Orc file itself.  No multi-threading is used in reading
 * off the Orc file using core Java commands.
 */
public class ParseTestOrc extends TestUtil {

    int totalFilesTested = 0;
    int numberWrong = 0;
    BufferedString h2o = new BufferedString();
    BufferedString tempOrc = new BufferedString();

    // list all orc files in smalldata/parser/orc directory
    private String[] allOrcFiles = {
            "smalldata/parser/orc/TestOrcFile.columnProjection.orc",
            "smalldata/parser/orc/bigint_single_col.orc",
            "smalldata/parser/orc/TestOrcFile.emptyFile.orc",
            "smalldata/parser/orc/bool_single_col.orc",
//      "smalldata/parser/orc/TestOrcFile.metaData.orc",
//      "smalldata/parser/orc/decimal.orc",
//      "smalldata/parser/orc/TestOrcFile.test1.orc",
            "smalldata/parser/orc/demo-11-zlib.orc",
            "smalldata/parser/orc/TestOrcFile.testDate1900.orc",
            "smalldata/parser/orc/demo-12-zlib.orc",
            "smalldata/parser/orc/TestOrcFile.testDate2038.orc",
            "smalldata/parser/orc/double_single_col.orc",
            "smalldata/parser/orc/TestOrcFile.testMemoryManagementV11.orc",
            "smalldata/parser/orc/float_single_col.orc",
            "smalldata/parser/orc/TestOrcFile.testMemoryManagementV12.orc",
            "smalldata/parser/orc/int_single_col.orc",
            "smalldata/parser/orc/TestOrcFile.testPredicatePushdown.orc",
            "smalldata/parser/orc/nulls-at-end-snappy.orc",
//      "smalldata/parser/orc/TestOrcFile.testSeek.orc",
//      "smalldata/parser/orc/orc-file-11-format.orc",
            "smalldata/parser/orc/TestOrcFile.testSnappy.orc",
            "smalldata/parser/orc/orc_split_elim.orc",
            "smalldata/parser/orc/TestOrcFile.testStringAndBinaryStatistics.orc",
//          "smalldata/parser/orc/over1k_bloom.orc",
            "smalldata/parser/orc/TestOrcFile.testStripeLevelStats.orc",
            "smalldata/parser/orc/smallint_single_col.orc",
//          "smalldata/parser/orc/TestOrcFile.testTimestamp.orc",
            "smalldata/parser/orc/string_single_col.orc",
//          "smalldata/parser/orc/TestOrcFile.testUnionAndTimestamp.orc",
            "smalldata/parser/orc/tinyint_single_col.orc",
            "smalldata/parser/orc/TestOrcFile.testWithoutIndex.orc",
//          "smalldata/parser/orc/version1999.orc"
    };

    @BeforeClass
    static public void setup() { TestUtil.stall_till_cloudsize(1); }

    @BeforeClass
    static public void _preconditionJavaVersion() { // NOTE: the `_` force execution of this check after setup
        // Does not run test on Java6 since we are running on Hadoop lib
        Assume.assumeTrue("Java6 is not supported", System.getProperty("java.version", "NA").startsWith("1.6"));
    }

    @Test
    public void testParseAllOrcs() {
        Set<String> failedFiles = new TreeSet<>();
        int numOfOrcFiles = allOrcFiles.length; // number of Orc Files to test

        for (int fIndex = 0; fIndex < numOfOrcFiles; fIndex++) {

//      if ((fIndex == 4) || (fIndex == 6) || (fIndex == 18) || (fIndex == 23) || (fIndex == 28))
//        continue;   // do not support metadata from user
//
//      if (fIndex == 31)   // contain only orc header, no column and no row, total file size is 0.
//        continue;
//
//      if (fIndex == 19)   // different column names are used between stripes
//        continue;
//
//      if (fIndex == 26)   // abnormal orc file, no inpsector structure available
//        continue;

//      if (fIndex ==30)    // problem getting the right column number and then comparison problem
//        continue;

//      if (fIndex == 22)     // problem with BufferedString retrieval for binary, wait for Tomas
//        continue;
//
//      if (fIndex == 17)   // problem with bigint retrieval, wait for Tomas
//        continue;

//      Random rn = new Random();
//      int randNum = rn.nextInt(10);
//
//      if (randNum > 3)  // skip test for 70% of the time
//        continue;

            String fileName = allOrcFiles[fIndex];
            Log.info("Orc Parser parsing " + fileName);
            File f = find_test_file_static(fileName);

            if (f != null && f.exists()) {
                org.apache.hadoop.conf.Configuration conf = new org.apache.hadoop.conf.Configuration();
                org.apache.hadoop.fs.Path p = new org.apache.hadoop.fs.Path(f.toString());
                try {
                    org.apache.hadoop.hive.ql.io.orc.Reader orcFileReader =
                        org.apache.hadoop.hive.ql.io.orc.OrcFile.createReader(p,
                                                                              org.apache.hadoop.hive.ql.io.orc.OrcFile.readerOptions(conf));
                    Frame h2oFrame = parse_test_file(fileName);     // read one orc file and build a H2O frame

                    numberWrong += compareH2OFrame(fileName, failedFiles, h2oFrame, orcFileReader);

                    if (h2oFrame != null) // delete frame after done.
                        h2oFrame.delete();

                    totalFilesTested++;

                } catch (IOException e) {
                    e.printStackTrace();
                    failedFiles.add(fileName);
                    numberWrong++;
                }

            } else {
                Log.warn("The following file was not found: " + fileName);
                failedFiles.add(fileName);
                numberWrong++;
            }
        }

        if (numberWrong > 0) {
            Log.warn("There are errors in your test.");
            assertEquals("Number of orc files failed to parse is: " + numberWrong + ", failed files = " +
                    failedFiles.toString(), 0, numberWrong);
        } else {
            Log.info("Parser test passed!  Number of files parsed is " + totalFilesTested);
        }
    }
}