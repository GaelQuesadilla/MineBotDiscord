from connections import autoTable

# Fields from autoTable
idField = autoTable.typeInt("id", notNull=True, primaryKey= True, autoIncrement= True)
userField = autoTable.typeStr("user", notNull=True)
titleField = autoTable.typeStr("titles", notNull=True)

fieldCoordinates_x = autoTable.typeInt("x_coordinates", notNull=True)
fieldCoordinates_y = autoTable.typeInt("y_coordinates")
fieldCoordinates_z = autoTable.typeInt("z_coordinates", notNull=True)

# Types of tables
tableCoordinates = (idField, titleField, fieldCoordinates_x, fieldCoordinates_y, fieldCoordinates_z, userField)
