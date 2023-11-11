import React from 'react';
import { useDragging } from '@src/hooks';
import { pluralRus } from '@src/utils';
import './file-uploader.less';

interface Props {
  classes?: string;
  disabled?: boolean;
  externalError?: string;
  handleChange?: (arg0: File[]) => void;
  files?: File[];
  maxCount?: number;
  maxSize?: number;
  minSize?: number;
  name?: string;
  onDraggingStateChange?: (dragging: boolean) => void;
  onDrop?: (arg0: File[]) => void;
  onSelect?: (arg0: File[]) => void;
  types?: string[];
}

export const FileUploader = ({
  classes = '',
  disabled = false,
  externalError = '',
  files,
  handleChange,
  maxCount = 1,
  maxSize,
  minSize = 0,
  name = 'files',
  onDraggingStateChange,
  onDrop,
  onSelect,
  types,
}: Props): React.ReactElement => {
  const accept = React.useMemo(() => `${(types ?? []).map(type => '.' + type)}`, [types]);
  const className = React.useMemo(() => `uploader-wrapper ${classes}${disabled ? ' is-disabled' : ''}`, [classes, disabled]);
  const inputRef = React.useRef<HTMLInputElement>(null);
  const labelRef = React.useRef<HTMLLabelElement>(null);
  const dragging = useDragging({ handleChange, inputRef, labelRef, maxCount, onDrop });
  const multiple = React.useMemo(() => maxCount > 1, [maxCount]);
  const [currentFiles, setFiles] = React.useState<File[]>([]);
  const [error, setError] = React.useState<string>('');
  const [uploaded, setUploaded] = React.useState<boolean>(false);

  const invalidFile = (file: File) => {
    const extension = file.name.split('.').pop()?.toLowerCase() ?? '';
    if (!types?.map((type: string) => type.toLowerCase()).includes(extension)) {
      setError('неподдерживаемый тип файла');
      return true;
    } else if (maxSize && file.size / 1048576 > maxSize) {
      setError('размер файла слишком большой');
      return true;
    } else if (minSize && file.size / 1048576 < minSize) {
      setError('размер файла слишком маленький');
      return true;
    } else {
      return false;
    }
  };

  const handleChanges = (fs: File[]): boolean => {
    if (fs && !fs.some(file => invalidFile(file))) {
      handleChange?.(fs);
      setError('');
      setFiles(fs);
      setUploaded(true);
      return true;
    } else {
      return false;
    }
  };

  const blockEvent = (e: React.MouseEvent<HTMLElement>) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleClick = (e: React.MouseEvent<HTMLInputElement>) => {
    e.stopPropagation();
    inputRef?.current?.click();
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(e.target.files).slice(0, maxCount);
    const success = handleChanges(files);
    if (onSelect && success) onSelect(files);
  };

  React.useEffect(() => {
    onDraggingStateChange?.(dragging);
  }, [dragging]);

  React.useEffect(() => {
    setError(externalError);
  }, [externalError]);

  React.useEffect(() => {
    if (files) {
      setFiles(files);
      setUploaded(true);
    } else {
      if (inputRef.current) inputRef.current.value = '';
      setFiles([]);
      setUploaded(false);
    }
  }, [files]);

  return (
    <>
      <label className={className} htmlFor={name} onClick={blockEvent} ref={labelRef}>
        <input
          accept={accept}
          disabled={disabled}
          multiple={multiple}
          name={name}
          onChange={handleInputChange}
          onClick={handleClick}
          ref={inputRef}
          type="file"
        />
        {dragging && (
          <div className="hover-message">
            <span>Переместить { multiple ? 'файлы' : 'файл' } сюда</span>
          </div>
        )}
        {(
          <>
            <div className={`file-icon file-icon-xls${disabled ? ' disabled' : ''}`}></div>
            {error ? (
              <span className="description" style={{ color: 'var(--error-color)' }}>
                Ошибка загрузки: {error}
              </span>
            ) : disabled ? (
              <span className="description">Невозможно сделать загрузку файлов</span>
            ) : currentFiles.length < 1 && !uploaded ? (
              <>
                <span className="description">
                  <u style={{ color: 'var(--primary-color)' }}>Выберите файл</u> или переместите его сюда
                </span>
                <span className="description">
                  Можно добавить { multiple ? 'до ' + pluralRus(maxCount, 'файла', 'файлов', 'файлов') : '1 файл' } в
                  формате .xls или .xlsx. Максимальный объём { multiple && <>каждого из файлов</> } – 10 Мб.
                </span>
              </>
            ) : (
              <span className="description">{ multiple ? 'Файлы успешно загружены!' : 'Файл успешно загружен!'}</span>
            )}
          </>
        )}
      </label>
    </>
  );
};
