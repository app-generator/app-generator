import React from 'react';
import { Button, Modal } from "flowbite-react";

const baseURL = window.location.origin;

export function Status({ open, handleClose, status, isError }) {
    return (
        <>
            <Modal show={open} onClose={handleClose}>
                <Modal.Header>Status</Modal.Header>
                <Modal.Body>
                    <div className="">
                        <span className="block text-base leading-relaxed text-gray-500 dark:text-gray-400">
                            <b>Status:</b> {status?.status}
                        </span>
                        <span className="block text-base leading-relaxed text-gray-500 dark:text-gray-400">
                            <b>Info:</b> {status?.info}
                        </span>
                    </div>
                </Modal.Body>
                <Modal.Footer>
                    {!isError ? (
                        <>
                            {(status?.gh_repo || status?.download_link) && (
                                <center>
                                    {status?.gh_repo && (
                                        <>
                                            Access the{' '}
                                            <a href={status.gh_repo} target="_blank" rel="noopener noreferrer">
                                                Generated Repository
                                            </a>
                                        </>
                                    )}

                                    {status?.gh_repo && status?.download_link && ' or '}

                                    {status?.download_link && (
                                        <>
                                            download the{' '}
                                            <a href={status.download_link} download>
                                                ZIP Archive
                                            </a>
                                        </>
                                    )}
                                </center>
                            )}
                        </>
                    ) : (
                        <center>
                            For assistance please contact{' '}
                            <a href={`${baseURL}/ticket/create/`}
                                target="_blank"
                                rel="django-generator"
                            >
                                support
                            </a>
                        </center>
                    )}
                </Modal.Footer>
            </Modal>
        </>
    );
}
