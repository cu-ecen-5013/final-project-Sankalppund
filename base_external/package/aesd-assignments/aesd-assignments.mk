
##############################################################
#
# AESD-ASSIGNMENTS
#
##############################################################

#TODO: Fill up the contents below in order to reference your assignment 3 git contents
AESD_ASSIGNMENTS_VERSION = daf618482f739c1ad5a6392418b1cb867241e6ae
AESD_ASSIGNMENTS_SITE = git@github.com:cu-ecen-5013/s20-remote-health-monitoring.git
AESD_ASSIGNMENTS_SITE_METHOD = git


define AESD_ASSIGNMENTS_BUILD_CMDS
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D) all
endef

#TODO: Add required executables or scripts below
define AESD_ASSIGNMENTS_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 $(@D)/humidity/humidity $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 0755 $(@D)/tmp102/tmp102 $(TARGET_DIR)/usr/bin
	$(INSTALL) -m 0755 $(@D)/humidity-start-stop.sh $(TARGET_DIR)/etc/init.d/S99humidity
endef


$(eval $(generic-package))
