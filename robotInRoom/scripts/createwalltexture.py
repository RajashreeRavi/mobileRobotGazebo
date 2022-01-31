import os

import charucoTextureGenerator


def createAndSaveTextureImages(modelMaterialsFolderPath, numberOfWalls):
	outputFolderPath = os.path.join(modelMaterialsFolderPath, "textures")
	os.makedirs(outputFolderPath, exist_ok=True)
	numberOfMarkers = 5
	pixelSize = 300
	charucoTextureGenerator.createWallTextureImage(outputFolderPath,
			numberOfMarkers, numberOfWalls, pixelSize)

def createAndSaveMaterialsFile(modelMaterialsFolderPath):
	materialFolderPath = os.path.join(modelMaterialsFolderPath, "scripts")
	for wall in range(numberOfWalls):
		wallString = f"{wall:04}"
		materialDict = {}
		materialText = """material aruco_wall{}
{{
  technique
  {{
    pass
    {{
      texture_unit
      {{
        texture ../textures/arucoMarker_{}.png
      }}
    }}
  }}
}}
		""".format(wallString, wallString)
		outputFilePath = os.path.join(materialFolderPath, f"aruco_wall{wall:02}.material")
		with open(outputFilePath, "w") as file:
			file.write(materialText)


if __name__=="__main__":
	modelMaterialsFolderPath = os.path.expanduser("~/git/mobileRobotGazebo/robotInRoom/models/simpleRoom/materials/")
	numberOfWalls = 4
	createAndSaveTextureImages(modelMaterialsFolderPath, numberOfWalls)
	createAndSaveMaterialsFile(modelMaterialsFolderPath)
