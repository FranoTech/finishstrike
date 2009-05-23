import unittest
import horus.core.computervision.featureExtraction as featureExtraction
import horus.core.computervision.image as image
from os.path import join, abspath, dirname
PREFIX = join(abspath(dirname(__file__)))

class FeatureExtractionTest(unittest.TestCase):

    def setUp(self):
        self.imagePath = join(PREFIX, "testImages/region_test_image.png")
        self.edPath = join(PREFIX,"testImages/edge_detection_test.png")
        self.edPath2 = join(PREFIX,"testImages/edge_detection_test2.png")
        self.edImage = image.Image(self.edPath)
        self.edImage2 = image.Image(self.edPath2)
        self.region_test_image = image.Image(self.imagePath)
    
    #XXX: Where is the doc string?
    def test_01_getRegionList(self):
        """
            Testing the getRegionList method. It divides the image 
            in 3x2 sub-images, which are represented by the matrixes 
            below, r0..r5. This method tests the amount of sub-images
            returned, and the pixel's color of each sub-image """
        r0 = [[0, 0 ,0, 0],
              [0, 0, 0, 0]]

        r1 = [[50, 50, 50, 50],
              [50, 50, 50, 50]]

        r2 = [[100, 100, 100, 100],
               [100, 100, 100, 100]]

        r3 = [[150, 150, 150, 150],
              [150, 150, 150, 150]]

        r4 = [[200, 200, 200, 200],
              [200, 200, 200, 200]]

        r5 = [[250, 250, 250, 250],
              [250, 250, 250, 250]]
        
        image_list = self.region_test_image.getRegionList(3, 2)
        self.assertEquals(len(image_list), 6)
        self.assertEquals(r0, image_list[0].pixel_matrix())
        self.assertEquals(r1, image_list[1].pixel_matrix())
        self.assertEquals(r2, image_list[2].pixel_matrix())
        self.assertEquals(r3, image_list[3].pixel_matrix())
        self.assertEquals(r4, image_list[4].pixel_matrix())      
        self.assertEquals(r5, image_list[5].pixel_matrix())
        
    def test_02_extractFeatureByEdgeDetection(self):
       featureMatrix = featureExtraction.extractFeatureByEdgeDetection(self.edImage)
       self.assertEquals(6, len(featureMatrix[0]))
       self.assertEquals(10, len(featureMatrix))
       self.assertEquals(1, featureMatrix[2][0], featureMatrix[0])
       self.assertEquals(1, featureMatrix[3][0], featureMatrix[0])
       self.assertEquals(1, featureMatrix[6][1], featureMatrix[6])
       self.assertEquals(1, featureMatrix[7][2], featureMatrix[7])
       self.assertEquals(1, featureMatrix[5][3], featureMatrix[5])
       self.assertEquals(1, featureMatrix[0][4], featureMatrix[0])
       self.assertEquals(1, featureMatrix[4][5], featureMatrix[4])

    def test_03_extractFeatureByEdgeDetection2(self):
        featureMatrix = featureExtraction.extractFeatureByEdgeDetection(self.edImage2)
        self.assertEquals(6, len(featureMatrix[0]))
        self.assertEquals(10, len(featureMatrix))
         
        self.assertEquals(1, featureMatrix[2][0])
        self.assertEquals(2, featureMatrix[3][0])
        self.assertEquals(1, featureMatrix[6][1])
        self.assertEquals(1, featureMatrix[7][2])
        self.assertEquals(1, featureMatrix[6][2])
        self.assertEquals(1, featureMatrix[5][3])
        self.assertEquals(1, featureMatrix[0][4])
        self.assertEquals(1, featureMatrix[4][5])

    def test_04_getTwoLoops(self):
        """
            Testing the number of loops, using the getNumLoops method.
        """
        image_path = join(PREFIX, 'testImages/two_squares.png')
        img = image.Image(image_path=image_path)
        self.assertEquals(2, featureExtraction.getNumLoops(img))
         
    def test_05_getThreeLoops(self):
        """
            Testing the number of loops, using the getNumLoops method.
        """
        imagePath = join(PREFIX, 'testImages/three_squares.png')
        imageP = image.Image(image_path= imagePath)
        self.assertEquals(3, featureExtraction.getNumLoops(imageP))
         
    def test_06_getTwoLoopsFromBCharacter(self):
        """
           This method tests the number of loops in a character B, 
           using the getNumLoops method.
        """
        image_path = join(PREFIX, 'testImages/b_character_skeletonized.png')
        image_b_character = image.Image(image_path=image_path)
        self.assertEquals(2, featureExtraction.getNumLoops(image_b_character))

    def test_07_blackIntensityInFourRegions(self):
        """
           This method tests the blackIntensity method.
           Comparing the intensity of black pixel in each blocks. As the
           blackIntensity has 2 defaul params (col=5, row=5), the result
           of this method is a matrix with 25 patterns.
        """
        image_path = join(PREFIX, 'testImages/black_intensity_test.png')
        img = image.Image(image_path)
        output_expected = [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,
                           0, 0, 0, 2, 1, 0, 3, 1, 0, 0, 0, 0, 0]
        self.assertEquals(featureExtraction.blocksIntensity(img),
                                            output_expected)
        
    def test_08_BlackIntensityFourNumber(self):
        """
            This method tests the blackIntensity method.
            Comparing the intensity of black pixel in each blocks. As the
            blackIntensity has 2 defaul params (col=5, row=5), the result
            of this method is a matrix with 25 patterns.
        """
        image_path = join(PREFIX,"testImages/black_intensity_test_number_four.png")
        img = image.Image(image_path=image_path)
        output_expected = [1, 0, 0, 0, 1, 4, 0, 0, 0, 4, 4, 0,
                     0, 0, 4, 1, 3, 3, 3, 5, 0, 0, 0, 0, 4]
        self.assertEquals(featureExtraction.blocksIntensity(img),
                                 output_expected)

if __name__=='__main__':
    unittest.main()

