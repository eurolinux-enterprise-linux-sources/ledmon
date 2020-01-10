/*
 * Intel(R) Enclosure LED Utilities
 * Copyright (C) 2011-2013 Intel Corporation.
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms and conditions of the GNU General Public License,
 * version 2, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin St - Fifth Floor, Boston, MA 02110-1301 USA.
 *
 */

#ifndef _SMP_H_INCLUDED
#define _SMP_H_INCLUDED

/**
 * @brief Sends message to SES processor of an enclosure.
 *
 * This function send a message to an enclosure in order to control LEDs of
 * the given slot/component. It uses interface of ENCLOSURE kernel module to
 * control LEDs.
 *
 * @param[in]      device         Path to an enclosure device in sysfs.
 * @param[in]      ibpi           IBPI pattern to visualize.
 *
 * @return Number of characters written if successful or -1 in case of error
 *         and errno is set to appropriate error code.
 */
int scsi_ses_write(struct block_device *device, enum ibpi_pattern ibpi);

/**
 * @brief Write message to outbound raw byte stream buffer.
 *
 * @param[in]      device         Path to a smp device in sysfs.
 * @param[in]      ibpi           IBPI pattern to visualize.
 *
 * @return 1 if successful or -1 in case of error
 *         and errno is set to appropriate error code.
 */
int scsi_smp_fill_buffer(struct block_device *device, enum ibpi_pattern ibpi);

/**
 * @brief Sends message to SMP device.
 *
 * This function triggers gpio order to control LEDs of
 * the given component.
 *
 * @param[in]      device         Path to a smp device in sysfs.
 *
 * @return Number of bytes written to device if successful or -1 in case of error
 *         and errno is set to appropriate error code.
 */
int scsi_smp_write_buffer(struct block_device *device);

/**
 * @brief Init smp and gets phy index,
 *
 * @param[in]      path            Path to the device in sysfs. It can be NULL
 *                                 to just initialize cntrl and not to get the
 *                                 phy.
 * @param[in]      cntrl           Controller device to be initialized.
 *
 * @return Phy index on success if path and cntrl weren't NULL
 *         0 if error occurred or path was NULL.
 */
int isci_cntrl_init_smp(const char *path, struct cntrl_device *cntrl);

#endif				/* _SCSI_H_INCLUDED_ */
