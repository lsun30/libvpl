LOCAL_PATH:= $(call my-dir)

##################################################################
include $(CLEAR_VARS)

LOCAL_SRC_FILES := \
	api1x_core/legacy-decode/src/legacy-decode.cpp

LOCAL_CPPFLAGS := \
    -std=c++11 \
    -DLIBVA_SUPPORT \
    -D_FORTIFY_SOURCE=2

LOCAL_CPPFLAGS += \
    -Wno-error \
    -Wno-missing-braces \
    -Wno-missing-field-initializers

LOCAL_C_INCLUDES := \
    coreAPI/legacy-decode/src \
    $(LOCAL_PATH)/../api \
    $(TARGET_OUT_HEADERS)/libva

LOCAL_MODULE := legacy-decode

LOCAL_SHARED_LIBRARIES := \
    libvpl \
    liblog \
    libva

LOCAL_PROPRIETARY_MODULE := true

include $(BUILD_EXECUTABLE)
##################################################################
include $(CLEAR_VARS)

LOCAL_SRC_FILES := \
    api1x_core/legacy-encode/src/legacy-encode.cpp

LOCAL_CPPFLAGS := \
    -std=c++11 \
    -DLIBVA_SUPPORT \
    -D_FORTIFY_SOURCE=2

LOCAL_CPPFLAGS += \
    -Wno-error \
    -Wno-missing-braces \
    -Wno-missing-field-initializers

LOCAL_C_INCLUDES := \
    coreAPI/legacy-encode/src \
    $(LOCAL_PATH)/../api \
    $(TARGET_OUT_HEADERS)/libva

LOCAL_MODULE := legacy-encode

LOCAL_SHARED_LIBRARIES := \
    libvpl \
    liblog \
    libva

LOCAL_PROPRIETARY_MODULE := true

include $(BUILD_EXECUTABLE)
##################################################################
include $(CLEAR_VARS)

LOCAL_SRC_FILES := \
    api1x_core/legacy-vpp/src/legacy-vpp.cpp

LOCAL_CPPFLAGS := \
    -std=c++11 \
    -DLIBVA_SUPPORT \
    -D_FORTIFY_SOURCE=2

LOCAL_CPPFLAGS += \
    -Wno-error \
    -Wno-missing-braces \
    -Wno-missing-field-initializers

LOCAL_C_INCLUDES := \
    coreAPI/legacy-vpp/src \
    $(LOCAL_PATH)/../api \
    $(TARGET_OUT_HEADERS)/libva

LOCAL_MODULE := legacy-vpp

LOCAL_SHARED_LIBRARIES := \
    libvpl \
    liblog \
    libva

LOCAL_PROPRIETARY_MODULE := true

include $(BUILD_EXECUTABLE)
##################################################################
