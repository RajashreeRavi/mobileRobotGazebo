import argparse
import os

import cv2
import numpy as np


def getMarkerFromDict(arucoDictName, markerId, pixels):
    arucoDict = cv2.aruco.Dictionary_get(arucoDictName)
    marker = np.zeros((pixels, pixels, 1), dtype="uint8")
    cv2.aruco.drawMarker(arucoDict, markerId, pixels, marker, borderBits=1)
    return marker


def createWallTextureImage(outputFolderPath, numberOfMarkers, numberOfWalls, pixelSize):
    ARUCO_DICT = {
        "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
        "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
        "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
        "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
        "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
        "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
        "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
        "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
        "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
        "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
        "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
        "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
        "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
        "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
        "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
        "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
        "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
        "DICT_APRIL_36h11": cv2.aruco.DICT_APRILTAG_36h11,
    }

    for wall in range(numberOfMarkers):
        frameSize = ((numberOfMarkers + 1) * 100) + (numberOfMarkers * pixelSize)
        emptyFrame = np.zeros((pixelSize * 2, frameSize, 1), dtype="uint8")
        emptyFrame[:, :, :] = 225
        chosenArucoDictionary = "DICT_APRIL_36h11"
        for markerId in range(wall * numberOfMarkers, (wall + 1) * numberOfMarkers):
            marker = getMarkerFromDict(ARUCO_DICT[chosenArucoDictionary], markerId,
                    pixelSize)
            colmStarter = markerId - (wall * numberOfMarkers)
            colm = (colmStarter + 1) * 100 + (colmStarter * pixelSize)
            row = int(pixelSize / 2)
            emptyFrame[row:row + pixelSize, colm:colm + pixelSize] = marker

        outputFileName = os.path.join(outputFolderPath, f"arucoMarker_{wall:04}.png")
        cv2.imwrite(outputFileName, emptyFrame)
        cv2.imshow("ArUco Marker", emptyFrame)
        cv2.waitKey(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=("This program creates and saves out aruco markers"))

    parser.add_argument("-m",
                        "--markers",
                        dest="numberOfMarkers",
                        help=("Number of markers that need to be generated"),
                        default=1,
                        type=int)
    parser.add_argument("-o",
                        "--outputFolderPath",
                        dest="outputFolderPath",
                        help=("Output folder path to save to"),
                        default=None,
                        type=str)
    parser.add_argument("-p",
                        "--pixelSize",
                        dest="pixelSize",
                        help=("Pixel size for each marker"),
                        default=300,
                        type=int)
    parser.add_argument("-w",
                        "--walls",
                        dest="numberOfWalls",
                        help=("Number of walls that need to be generated"),
                        default=1,
                        type=int)
    args = parser.parse_args()

    if not args.outputFolderPath:
        raise IOError("Invalid None outputFolderPath")

    outputFolderPath = os.path.expanduser(args.outputFolderPath)
    os.makedirs(outputFolderPath, exist_ok=True)
    createWallTextureImage(outputFolderPath, args.numberOfMarkers, args.numberOfWalls, args.pixelSize)
