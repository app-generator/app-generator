import React from 'react';
import { Button, Modal } from "flowbite-react";

export function Status({ open, handleClose, status }) {
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
                    <center>
                        Access the{' '}
                        <a  href={status?.gh_repo}
                            target="_blank"
                            rel="noopener noreferrer"
                        > 
                        Generated Repository
                        </a>
                        {' '}or download the{' '}
                        <a  href={status?.download_link}
                            download 
                        > 
                        ZIP Archive
                        </a> 
                    </center>
                </Modal.Footer>
            </Modal>
        </>
    );
}
