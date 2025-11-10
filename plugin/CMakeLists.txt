list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

project(HelloPlugin)
if (USE_THUNDER_R5)
    find_package(Thunder REQUIRED)
else ()
    find_package(WPEFramework REQUIRED)
endif (USE_THUNDER_R5)

find_package(WPEFramework REQUIRED)
find_package(${NAMESPACE}Core REQUIRED)
find_package(${NAMESPACE}Plugins REQUIRED)

set(MODULE_NAME ${NAMESPACE}HelloPlugin)
include(CmakeHelperFunctions)

# Build the main plugin that runs inside the WPEFramework daemon
add_library(${MODULE_NAME} SHARED HelloPlugin.cpp)

target_link_libraries(${MODULE_NAME}  PRIVATE
                      ${NAMESPACE}Core::${NAMESPACE}Core
                      ${NAMESPACE}Plugins::${NAMESPACE}Plugins)

set_target_properties(${MODULE_NAME} PROPERTIES
                      CXX_STANDARD 11
                      CXX_STANDARD_REQUIRED YES)

if (USE_THUNDER_R5)
    install(TARGETS ${MODULE_NAME} DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/thunder/plugins)
else ()
    install(TARGETS ${MODULE_NAME} DESTINATION ${CMAKE_INSTALL_PREFIX}/lib/wpeframework/plugins)
endif (USE_THUNDER_R5)

write_config()
