import { RefObject, useCallback, useEffect, useState } from 'react';

let draggingCount = 0;

interface Props {
  handleChange?: (arg0: File[]) => void;
  inputRef: RefObject<HTMLInputElement>;
  labelRef: RefObject<HTMLLabelElement>;
  maxCount: number;
  onDrop?: (arg0: File[]) => void;
}

export const useDragging = ({ handleChange, inputRef, labelRef, maxCount, onDrop }: Props): boolean => {
  const [dragging, setDragging] = useState(false);
  const handleClick = useCallback(() => inputRef.current.click(), [inputRef]);

  const handleDragIn = useCallback((e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    draggingCount++;
    if (e.dataTransfer?.items?.length > 0) setDragging(true);
  }, []);

  const handleDragOut = useCallback((e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    draggingCount--;
    if (draggingCount < 1) setDragging(false);
  }, []);

  const handleDrag = useCallback((e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
  }, []);

  const handleDrop = useCallback((e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragging(false);
    draggingCount = 0;
    const files = e.dataTransfer?.files;
    if (files?.length > 0) {
      const result = Array.from(files).slice(0, maxCount);
      handleChange?.(result);
      onDrop?.(result);
    }
  }, [handleChange]);

  useEffect(() => {
    const element = labelRef.current;
    element.addEventListener('click', handleClick);
    element.addEventListener('dragenter', handleDragIn);
    element.addEventListener('dragleave', handleDragOut);
    element.addEventListener('dragover', handleDrag);
    element.addEventListener('drop', handleDrop);
    return () => {
      element.removeEventListener('click', handleClick);
      element.removeEventListener('dragenter', handleDragIn);
      element.removeEventListener('dragleave', handleDragOut);
      element.removeEventListener('dragover', handleDrag);
      element.removeEventListener('drop', handleDrop);
    };
  }, [handleClick, handleDragIn, handleDragOut, handleDrag, handleDrop, labelRef]);

  return dragging;
}
